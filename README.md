# GovDataHub

A modern FastAPI + SQLAlchemy (async) backend for government data aggregation and analytics.

---

## Features
- FastAPI app with async SQLAlchemy ORM
- PostgreSQL database (asyncpg driver)
- Alembic migrations
- Modular src/ layout
- Automated tests with pytest

---

## Quickstart

### 1. Clone & Install
```sh
git clone <your-repo-url>
cd govdatahub
python3 -m pip install .
```

### 2. Configure Environment
- Copy `.env.example` to `.env` and edit as needed (or set env vars directly)
- Default DB: `postgresql+asyncpg://localhost/govdatahub_local`

### 3. Database Setup
```sh
createdb govdatahub_local
alembic upgrade head
```

### 4. Run the App
```sh
make run
# or
uvicorn src.gdhub.main:app --reload
```

### 5. Run Tests
```sh
make test
# or
PYTHONPATH=src python3 -m pytest
```

---

## Project Structure
```
/ (repo root)
├── src/
│   └── gdhub/
│       ├── main.py         # FastAPI app
│       ├── db.py           # Async SQLAlchemy engine/session
│       ├── models.py       # ORM models
│       ├── config.py       # Pydantic settings
│       ├── routers/        # API routers
│       └── ...
├── alembic/                # DB migrations
├── tests/                  # Pytest tests
├── Makefile
├── pyproject.toml
└── README.md
```

---

## Common Commands
- `make run`      — Start the FastAPI app
- `make test`     — Run all tests
- `make lint`     — Lint/format code (if configured)
- `alembic revision --autogenerate -m "msg"` — Create migration
- `alembic upgrade head` — Apply migrations

---

## Contributing
- Fork, branch, and PR as usual
- Write tests for new features
- Keep code formatted and linted

---

## License
MIT (or your license here)
