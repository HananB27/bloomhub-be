# BloomHub Backend (Django)

Django backend with the same tooling as the frontend: tests, formatting, GitStream, and commit convention `[BHB-XX]`.

## Local setup

- Python 3.11+
- Create a venv and install: `pip install -r requirements.txt`
- Copy `.env.example` to `.env` and set `DATABASE_URL` (local Postgres or Neon dev).
- Run migrations: `python manage.py migrate`
- Start the server: `python manage.py runserver` (or `python manage.py runserver 8001` if port 8000 is in use).
- Install pre-commit: `pre-commit install` (and `pre-commit install --hook-type commit-msg` for commit message check).

## Scripts

- **Lint:** `ruff check .`
- **Format:** `black .` / `black --check .`
- **Tests:** `pytest`

## Docs

- **Migrations on dev:** `docs/MIGRATIONS_DEV.md`
- **Production deploy:** `docs/DEPLOY_PRODUCTION.md`
- **Branch protection:** `docs/BRANCH_PROTECTION.md`
