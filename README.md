# 🏗️ FastAPI Production-Ready App

This repository showcases a robust backend API built with **FastAPI**, featuring clean architecture, authentication, PostgreSQL integration, and modularized routing — all with a focus on production readiness.

> This is a hands-on project. Progressively building from basics to CI/CD & deployment.

---

## ✅ Features Completed

* 🔧 **Project Setup**

  * Python virtual environments (Mac & Windows)
  * Dependency management via `pip`
  * Modular FastAPI app structure

* 🚀 **Core FastAPI Concepts**

  * Path operations (GET, POST, DELETE, PUT)
  * Response models with **Pydantic**
  * Built-in Swagger docs for testing

* 💾 **PostgreSQL Integration**

  * Schema and table creation
  * SQL queries (raw & ORM via SQLAlchemy)
  * Environment variables for DB config

* 🧱 **SQLAlchemy ORM**

  * Models, session management, and CRUD operations
  * Timestamps, filtering, and relationships

* 🛡️ **Authentication**

  * User registration with password hashing using `passlib[argon2]`
  * Login endpoint using OAuth2 `PasswordRequestForm`
  * JWT token generation & decoding with `python-jose[cryptography]`
  * Verified route protection using `Depends(get_current_user)`
  * Advanced Postman usage (collections, tokens, headers)

---

## 🔜 Upcoming Features

* 🧩 User relationships and post ownership
* 🔘 Vote/Like system (and preventing duplicate votes)
* 🔁 Alembic DB migrations
* ✅ GitHub CI/CD pipeline with testing
* 🐳 Docker-based deployment (Heroku & Ubuntu)

---

## 📦 Tech Stack

* **FastAPI** (Backend Framework)
* **PostgreSQL** (Relational DB)
* **SQLAlchemy** (ORM)
* **Pydantic** (Data validation)
* **Passlib** (Password hashing)
* **JWT via python-jose** (Authentication)
* **Docker, GitHub Actions** (Deployment & CI/CD - upcoming)

---

## 🗂️ Project Structure (so far)

```
app/
├── main.py
├── database.py
├── models.py
├── schemas.py
├── oauth2.py              # JWT logic
├── utils.py               # password hashing
├── routers/
│   ├── users.py
│   ├── posts.py
│   └── auth.py            # login route
```

---

## 🚀 Setup Instructions

```bash
# Clone the repo
git clone https://github.com/your-username/fastapi-production-ready-app.git
cd fastapi-production-ready-app

# Create virtual env
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows

# Run the app
uvicorn app.main:app --reload
```

---
