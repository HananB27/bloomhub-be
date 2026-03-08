# BloomHub Backend (Django)

Django backend with tests, formatting, and commit convention `[BHB-XX]`.

---

## Local setup

### Prerequisites

- Python 3.11+ (3.12 recommended)

### Run locally

```bash
git clone <repo-url>
cd BloomHub-be
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt
cp .env.example .env
```

Edit `.env`:

- **SQLite (easiest):** leave `DATABASE_URL` unset. The app uses `db.sqlite3` in the project root.
- **Local Postgres:** set `DATABASE_URL=postgres://user:password@localhost:5432/yourdb`

Then:

```bash
python manage.py migrate
python manage.py runserver
```

Open http://127.0.0.1:8000/

### Pre-commit (optional)

Runs ruff, black, and pytest on every commit; commit is blocked if they fail.

```bash
pre-commit install
pre-commit install --hook-type commit-msg
```

---

## Scripts

| Command | Description |
|--------|-------------|
| `ruff check .` | Lint |
| `black .` / `black --check .` | Format / check format |
| `pytest` | Run tests |
