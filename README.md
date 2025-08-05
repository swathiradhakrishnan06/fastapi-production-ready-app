# 🏗️ FastAPI Production-Ready App

This repository showcases a robust backend API built with **FastAPI**, featuring clean architecture, authentication, PostgreSQL integration, and modularized routing — all with a focus on production readiness.

> 🛠️ Covers hands-on backend concepts step-by-step — from basics to Docker & CI/CD.

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

* 🔐 **Authentication & Authorization**
  * User registration with password hashing via `passlib[argon2]`
  * OAuth2 Login with JWT using `python-jose[cryptography]`
  * Protected routes via `Depends(get_current_user)`
  * Post ownership enforcement
  * Role-based logic: update/delete own posts only
  * Voting system (like/unlike a post)

* 🧬 **Alembic Migrations**
  * Auto-generate DB migration scripts
  * Apply schema changes incrementally

---

## 🔜 Upcoming Features

* ✅ Deployment to **Heroku** (Section 13)
* 🐧 Deployment on Ubuntu VM with NGINX + Gunicorn
* 🐳 Docker + Docker Compose setup
* 🔁 GitHub Actions for CI/CD & test automation
* 🔬 Full test coverage via `pytest` and fixtures

---

## 📦 Tech Stack

* **FastAPI** (Backend Framework)
* **PostgreSQL** (Relational DB)
* **SQLAlchemy** (ORM)
* **Pydantic** (Validation)
* **Passlib** (Hashing)
* **JWT** via `python-jose`
* **Docker**, **Alembic**, **GitHub Actions**

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
├── config.py              # env vars via pydantic-settings
├── routers/
│   ├── users.py
│   ├── posts.py
│   ├── auth.py            # login
│   └── vote.py            # like/unlike logic

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

📘 Want full explanations, SQLAlchemy vs Pydantic insights, and JWT code examples?

→ [DETAILED\_README.md](./DETAILED_README.md)

```

---