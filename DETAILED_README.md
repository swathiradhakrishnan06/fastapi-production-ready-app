# 📘 DETAILED\_README.md

This document is a deeper dive into the codebase and concepts covered in the FastAPI production-ready application. It explains each topic progressively, with reasoning and examples.

---

## 📂 Project Structure (So far)

```bash
app/
├── main.py                  # Entry point, sets up app and routers
├── database.py              # SQLAlchemy engine and session setup
├── models.py                # SQLAlchemy models (tables)
├── schemas.py               # Pydantic models (request/response validation)
├── utils.py                 # Password hashing utility functions
├── oauth2.py                # Token creation & validation (OAuth2 + JWT)
├── config.py                # Environment variable management (via pydantic-settings)
├── routers/                 # Modular routes
│   ├── users.py             # User registration and login
│   ├── posts.py             # CRUD operations for posts
│   ├── auth.py              # OAuth2 login route
│   └── vote.py              # Like/Unlike system
```

---

## ⚙️ FastAPI Basics

FastAPI uses **Python decorators** to associate routes with Python functions, similar to Flask. Here’s a basic example:

### Path Operation Example

```python
@app.get("/posts")
def get_posts():
    return {"message": "All posts"}
```

* `@app.get("/posts")`: Handles GET requests to `/posts`
* `return`: Response will be auto-converted to JSON

All operations (GET, POST, PUT, DELETE) follow similar patterns.

---

## 🧰 Pydantic Models vs SQLAlchemy Models

### Purpose:

* **Pydantic models (schemas)**: Used for request/response validation
* **SQLAlchemy models**: Used for database schema and queries

### `schemas.py` (Pydantic - for validation)

```python
class PostBase(BaseModel):
    title: str
    content: str
    published: bool = True

class Post(PostBase):
    id: int
    created_at: datetime
    owner_id: int
    owner: UserOut

    class Config:
        from_attributes = True
```

### `models.py` (SQLAlchemy - for DB)

```python
class Post(Base):
    __tablename__ = "posts"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    content = Column(String, nullable=False)
    published = Column(Boolean, default=True)
    created_at = Column(TIMESTAMP(timezone=True), server_default=text('now()'))
    owner_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False)

    owner = relationship("User")
```

### 🔹 Side Note: `from_attributes`

This is required to allow Pydantic to generate responses directly from SQLAlchemy objects (i.e. when returning a DB model).

### 🗒️ Extra Insight: Response vs Request Models

* Use response models (like `Post`) to **shape what is returned to clients**, often hiding sensitive/internal fields.
* Use request models (like `PostCreate`) to **validate what the client sends**, containing only required input fields.

---

## 🔐 Password Hashing

User passwords are hashed using `passlib` before saving to the database.

### `utils.py`

```python
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash(password: str):
    return pwd_context.hash(password)

def verify(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)
```

This helps secure user credentials by storing hashed passwords only.

---

## 👤 User Registration

### `schemas.py`

```python
class UserCreate(BaseModel):
    email: EmailStr
    password: str
```

### `routers/users.py`

```python
@router.post("/users", response_model=UserOut)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    hashed_password = utils.hash(user.password)
    new_user = models.User(email=user.email, password=hashed_password)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user
```

---

## 🔑 JWT + OAuth2

We use OAuth2PasswordBearer flow with JWT for stateless authentication.

### OAuth2PasswordRequestForm (Login Form Parser)

```python
from fastapi.security import OAuth2PasswordRequestForm
```

This allows you to parse form data like:

```
username=email@example.com
password=123456
```

### Login Route (routers/auth.py)

```python
@router.post("/login")
def login(user_credentials: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.email == user_credentials.username).first()
    if not user or not utils.verify(user_credentials.password, user.password):
        raise HTTPException(status_code=403, detail="Invalid Credentials")

    access_token = oauth2.create_access_token(data={"user_id": user.id})
    return {"access_token": access_token, "token_type": "bearer"}
```

---

## 🌐 Route Protection

Protected routes require a valid token passed via the `Authorization: Bearer <token>` header.

### `oauth2.py` (continued)

```python
from fastapi import Depends, status, HTTPException
from fastapi.security import OAuth2PasswordBearer

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    credentials_exception = HTTPException(status_code=401, detail="Could not validate credentials")
    return verify_access_token(token, credentials_exception)
```

### In routes:

```python
@router.get("/posts", response_model=List[schemas.Post])
def get_posts(current_user: int = Depends(oauth2.get_current_user)):
    return db.query(models.Post).filter(models.Post.owner_id == current_user.id).all()
```

### 🔹 Note:

* Only authenticated users can access this route
* Filter by `owner_id` ensures users only see their own posts

---

## 🔠 Ownership-based Authorization

Update/delete routes verify ownership:

```python
if post.owner_id != current_user.id:
    raise HTTPException(status_code=403, detail="Not authorized to perform this action")
```

---

## ❤️ Vote/Like System

Users can like/unlike posts — but only once.

### `schemas.py`

```python
class Vote(BaseModel):
    post_id: int
    dir: conint(le=1)
```

### `routers/vote.py`

```python
@router.post("/vote", status_code=201)
def vote(vote: Vote, db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user)):
    vote_query = db.query(models.Vote).filter(
        models.Vote.post_id == vote.post_id,
        models.Vote.user_id == current_user.id
    )
    found_vote = vote_query.first()

    if vote.dir == 1:
        if found_vote:
            raise HTTPException(status_code=409, detail="Vote already exists")
        new_vote = models.Vote(post_id=vote.post_id, user_id=current_user.id)
        db.add(new_vote)
        db.commit()
        return {"message": "Vote added successfully"}
    else:
        if not found_vote:
            raise HTTPException(status_code=404, detail="Vote does not exist")
        vote_query.delete(synchronize_session=False)
        db.commit()
        return {"message": "Vote deleted successfully"}
```

### 🔹 Insight:

* `dir=1` means upvote
* Else block acts like a toggle — remove vote if exists

---

## 🧬 Alembic Migrations

To track schema changes incrementally:

```bash
alembic init alembic
# Configure alembic.ini and env.py
alembic revision --autogenerate -m "add user_id to posts"
alembic upgrade head
```
---

## ☁️ Deployment Progress: EC2 + RDS

### ✅ Steps Completed:

1. **Created EC2 instance** (Ubuntu 22.04)

   * Enabled inbound security rule for port 22 (SSH) and 8000 (Uvicorn)

2. **Connected to EC2 via SSH** using `.pem` key

   * Updated system, installed Python 3.12, `venv`, `git`, and `pip`

3. **Cloned GitHub repo and set up virtual environment**

```bash
git clone https://github.com/swathiradhakrishnan06/fastapi-production-ready-app.git
cd fastapi-production-ready-app
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

4. **Created `.env` file** with RDS credentials

```env
DATABASE_HOST=<rds-endpoint>
DATABASE_PORT=5432
DATABASE_NAME=fastapi
DATABASE_USER=postgres
DATABASE_PASSWORD=password123
SECRET_KEY=<your-secret>
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
```

5. **Configured RDS PostgreSQL instance**

   * Created via AWS RDS Console
   * Set public access + added security group rule for port 5432 from anywhere (for dev)
   * Created `fastapi` database inside RDS using pgAdmin or `psql`

6. **Ran Alembic Migrations from EC2 to RDS**

```bash
alembic upgrade head
```

✅ Migrations succeeded and created all tables.

7. **Started FastAPI app with Uvicorn**

```bash
uvicorn app.main:app --host 0.0.0.0 --port 8000
```

* Accessed from browser: `http://<ec2-public-ip>:8000`

---
## 🔐 Security Notes

> 🚨 Important: You should NOT expose RDS publicly in production.

* Add more secure inbound rules (e.g. allow 5432 only from EC2 IP)
* Use `.env.example` to share structure without secrets

---

## 🔁 What’s Next?

* Option 1: Setup **Gunicorn + NGINX** on EC2 for production-ready API
* Option 2: Migrate to **AWS Lambda + API Gateway** (serverless)
* Option 3: Add **Terraform** to provision infra automatically

---

🔗 [Back to Main README](./README.md)

## 🔖 Summary So Far

* ✅ FastAPI routing and modular architecture
* ✅ Pydantic models for validation and response shaping
* ✅ SQLAlchemy for database interaction (CRUD)
* ✅ Password hashing using `passlib`
* ✅ JWT-based login using OAuth2PasswordRequestForm
* ✅ Protected routes
* ✅ Route-level authorization (ownership)
* ✅ Vote/Like system
* ✅ SQLAlchemy relationships (User <-> Posts)
* ✅ Alembic migrations for schema versioning
* ✅ Deployment: EC2 + RDS
