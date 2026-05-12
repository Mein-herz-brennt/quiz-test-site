# Quiz Site 🎓

A **REST API backend** for an online quiz/test platform built with **FastAPI** and **SQLAlchemy 2.0**. The application supports user registration, JWT-based authentication, and a full quiz flow — creating quizzes, managing questions and answers, and recording results.

---

## 🛠️ Tech Stack

| Layer | Technology |
|---|---|
| Framework | FastAPI 0.135+ |
| ORM | SQLAlchemy 2.0 |
| Migrations | Alembic 1.18+ |
| Validation | Pydantic 2.12+ |
| Server | Uvicorn 0.41+ |
| Auth | JWT (PyJWT) + bcrypt |
| Database | SQLite (development) |
| Config | python-decouple |

---

## 📁 Project Structure

```
quiz-test-site/
├── alembic/                        # Database migration scripts
│   └── versions/
├── src/
│   ├── api/
│   │   ├── v1/
│   │   │   ├── auth.py             # Auth endpoints (register, login)
│   │   │   └── quests.py           # Quiz/question endpoints
│   │   └── router.py               # API v1 router aggregation
│   ├── core/
│   │   ├── config.py               # App settings via python-decouple
│   │   ├── database.py             # SQLAlchemy engine and session
│   │   ├── dependencies.py         # FastAPI dependency injections
│   │   └── security.py             # JWT creation and password hashing
│   ├── modules/
│   │   ├── auth/
│   │   │   ├── schemas.py          # Login/register Pydantic schemas
│   │   │   └── service.py          # Auth business logic
│   │   ├── quest/
│   │   │   ├── models/
│   │   │   │   ├── answers.py      # Answer ORM model
│   │   │   │   ├── questions.py    # Question ORM model
│   │   │   │   ├── quizzes.py      # Quiz ORM model
│   │   │   │   └── results.py      # Result ORM model
│   │   │   ├── repositories/
│   │   │   │   ├── base.py         # Base repository (generic CRUD)
│   │   │   │   ├── answer.py
│   │   │   │   ├── question.py
│   │   │   │   ├── quiz.py
│   │   │   │   └── result.py
│   │   │   ├── schemas/
│   │   │   │   ├── quiz.py         # Quiz request/response schemas
│   │   │   │   └── submission.py   # Answer submission schemas
│   │   │   └── services/
│   │   │       ├── question.py     # Question business logic
│   │   │       ├── quiz.py         # Quiz business logic
│   │   │       └── result.py       # Result calculation logic
│   │   └── users/
│   │       ├── models.py           # User ORM model
│   │       ├── repositories.py     # User DB queries
│   │       ├── schemas.py          # User Pydantic schemas
│   │       └── services.py         # User business logic
│   └── main.py                     # FastAPI app entry point
├── .env                            # Environment variables (not committed)
├── .gitignore
├── requirements.txt
└── README.md
```

---

## ⚙️ Requirements

- Python **3.10+**
- pip

---

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/Mein-herz-brennt/quiz-test-site.git
cd quiz-test-site
```

### 2. Create and activate a virtual environment

```bash
python -m venv venv

# Linux / macOS
source venv/bin/activate

# Windows
venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure environment variables

Create a `.env` file in the project root:

```env
DATABASE_URL=sqlite:///./quiz.db
SECRET_KEY=your-very-secret-key-here
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
```

> `python-decouple` loads these values automatically from `.env` via `core/config.py`.

### 5. Run database migrations

```bash
alembic upgrade head
```

> `alembic.ini` is excluded from version control since it contains the database URL. If it's missing, run `alembic init alembic` and set `sqlalchemy.url` to your `DATABASE_URL`.

### 6. Start the development server

```bash
uvicorn src.main:app --reload
```

The API will be available at **http://127.0.0.1:8000**

---

## 📖 API Documentation

FastAPI generates interactive documentation automatically:

| Interface | URL |
|---|---|
| Swagger UI | http://127.0.0.1:8000/docs |
| ReDoc | http://127.0.0.1:8000/redoc |

---

## 🔐 Authentication

The API uses **JWT Bearer tokens**.

1. Register a new account: `POST /api/v1/auth/register`
2. Log in to receive a token: `POST /api/v1/auth/login`
3. Pass the token in the `Authorization` header on protected routes:

```
Authorization: Bearer <your_token>
```

Passwords are hashed with **bcrypt** and never stored in plain text. Token signing and verification are handled in `core/security.py`.

---

## 🧩 Architecture

The project follows a **layered architecture** with clear separation of concerns:

```
API layer        (src/api/v1/)
      ↓
Service layer    (modules/*/services/)      ← business logic
      ↓
Repository layer (modules/*/repositories/) ← database queries
      ↓
Model layer      (modules/*/models/)       ← SQLAlchemy ORM tables
```

- **`core/`** — shared infrastructure: database session, app config, security utilities, and FastAPI dependencies
- **`modules/auth/`** — registration and login logic
- **`modules/quest/`** — full quiz lifecycle: quizzes, questions, answers, submissions, and results
- **`modules/users/`** — user account management

---

## 🗄️ Database Migrations

Alembic manages all schema changes:

```bash
# Generate a new migration after editing models
alembic revision --autogenerate -m "describe your change"

# Apply all pending migrations
alembic upgrade head

# Roll back one step
alembic downgrade -1
```

---

## 📦 Dependencies

```
SQLAlchemy~=2.0.48
alembic~=1.18.4
pydantic~=2.12.5
fastapi~=0.135.1
uvicorn~=0.41.0
bcrypt
python-decouple
pyjwt
python-multipart
```

---

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/your-feature`
3. Commit your changes: `git commit -m "Add your feature"`
4. Push to the branch: `git push origin feature/your-feature`
5. Open a Pull Request
