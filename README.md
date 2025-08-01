# 🏗️ FastAPI Production-Ready App

This repository showcases a robust backend API built with **FastAPI**, featuring clean architecture, authentication, PostgreSQL integration, and modularized routing — all with a focus on production readiness.

> This is a hands-on project. Progressively building from basics to CI/CD & deployment.

---

## ✅ Features Completed 

- 🔧 **Project Setup**  
  - Python virtual environments (Mac & Windows)
  - Dependency management via `pip`
  - Modular FastAPI app structure

- 🚀 **Core FastAPI Concepts**
  - Path operations (GET, POST, DELETE, PUT)
  - Response models with **Pydantic**
  - Built-in Swagger docs for testing

- 💾 **PostgreSQL Integration**
  - Schema and table creation
  - SQL queries (raw & ORM via SQLAlchemy)
  - Environment variables for DB config

- 🧱 **SQLAlchemy ORM**
  - Models, session management, and CRUD operations
  - Timestamps, filtering, and relationships

- 🛡️ **Authentication (in progress)**
  - User registration with hashed passwords (via `passlib[argon2]`)
  - Modular router for user operations
  - ✅ JWT Token Basics introduced

---

## 🔜 Upcoming Features

- 🔑 OAuth2 Login Flow (with Password Grant)
- Token creation, verification, and route protection
- Vote/Like system and relationships
- Alembic migrations
- CI/CD with GitHub Actions
- Docker-based deployment (Heroku & Ubuntu)

---

## 📦 Tech Stack

- **FastAPI** (Backend Framework)
- **PostgreSQL** (Relational DB)
- **SQLAlchemy** (ORM)
- **Pydantic** (Data validation)
- **Passlib** (Password hashing)
- **JWT** (Authentication)
- **Docker, GitHub Actions** (Deployment & CI/CD - planned)

---

## 🗂️ Project Structure (so far)

```

app/
├── main.py
├── database.py
├── models.py
├── schemas.py
├── utils.py               # password hashing
├── routers/
│   ├── users.py
│   └── posts.py

````

---

## 🚀 Setup Instructions

```bash
# Clone the repo
git clone https://github.com/your-username/fastapi-production-ready-app.git
cd fastapi-production-ready-app

# Create virtual env
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows

# Install dependencies
pip install -r requirements.txt

# Run the app
uvicorn app.main:app --reload
````

---

