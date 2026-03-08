# Migrations on Dev

## When do migrations run on dev?

- **Automatically** when you push to the `dev` branch **and** the push includes changes under `**/migrations/**/*.py` (excluding `__init__.py`).
- Workflow: `.github/workflows/migrate-dev.yml`.

## What you need to do

1. **Add secret `DEV_DATABASE_URL`** in the backend repo:
   - **Settings** → **Secrets and variables** → **Actions** → **New repository secret**
   - Name: `DEV_DATABASE_URL`
   - Value: your Neon **dev** branch connection string (e.g. `postgresql://...@ep-xxx-pooler.../neondb?sslmode=require`).
   - Use the URL from your Neon dashboard for the **dev** branch; do not commit it in the repo.

2. Use a **`dev`** branch for development. When you merge or push migration files to `dev`, the workflow runs `python manage.py migrate --noinput` against the dev database.

3. Ensure your Django project has **`manage.py`** in the repo root (or update the workflow `run` to use the correct path, e.g. `python config/manage.py` if you use a config package).

## If your app layout is different

- If `manage.py` lives in a subfolder (e.g. `config/`), change the migrate step in `.github/workflows/migrate-dev.yml` to:
  `run: python config/manage.py migrate --noinput`
- If you use a different branch name for dev, change `branches: [dev]` in the workflow to match.
