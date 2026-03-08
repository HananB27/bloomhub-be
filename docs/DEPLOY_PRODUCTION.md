# Pushing to Production

## How production deploy is triggered

- **Option A – Push to `main`:** Pushing or merging to `main` runs the **Deploy Production** workflow (`.github/workflows/deploy-production.yml`). It:
  1. Runs **migrations** against the production database (using `PROD_DATABASE_URL`).
  2. Then you add your actual deploy step (e.g. deploy to Railway, Render, Fly, or a server).

- **Option B – Manual run:** You can also run the same workflow from the **Actions** tab → **Deploy Production** → **Run workflow**.

## What you need to do

1. **Add secret `PROD_DATABASE_URL`**
   - **Settings** → **Secrets and variables** → **Actions**
   - New repository secret: `PROD_DATABASE_URL` = your Neon **production** (root branch) connection string.
   - Use the URL from your Neon dashboard; never commit it in the repo.

2. **Optional: GitHub Environment “production”**
   - **Settings** → **Environments** → **New environment** → name it `production`.
   - You can add protection rules (e.g. required reviewers) so production only deploys after approval.
   - In the workflow we use `environment: production` so it uses this environment and its secrets.

3. **Add your deploy step**
   - Edit `.github/workflows/deploy-production.yml`.
   - After the “Run migrations (production)” step, add the step that deploys your app, for example:
     - **Railway:** use `railway up` or Railway’s GitHub integration.
     - **Render:** use Render’s GitHub integration or their API/CLI.
     - **Fly.io:** `fly deploy`.
     - **VPS:** SSH + pull + restart gunicorn/systemd.

So: **production push = merge to `main` (or manual run)** → workflow runs prod migrations → you add your deploy step to complete the push.
