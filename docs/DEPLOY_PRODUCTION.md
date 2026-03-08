# Pushing to Production

## How production deploy is triggered

Production deploys **only when you run the workflow manually**:

1. Open the repo on GitHub → **Actions**
2. Select **Deploy Production** in the left sidebar
3. Click **Run workflow** (dropdown on the right) → **Run workflow**

The workflow will:

1. Run **migrations** against the production database (using `PROD_DATABASE_URL`)
2. Run the **Deploy to production** step (add your real deploy command in the workflow)

## What you need to do

1. **Add secret `PROD_DATABASE_URL`**  
   **Settings** → **Secrets and variables** → **Actions** → New repository secret: `PROD_DATABASE_URL` = your Neon production connection string.

2. **Optional: GitHub Environment “production”**  
   **Settings** → **Environments** → New environment → name it `production`. You can add protection rules (e.g. required reviewers). The workflow uses `environment: production`.

3. **Add your deploy step**  
   Edit `.github/workflows/deploy-production.yml` and replace the placeholder “Deploy to production” step with your host’s deploy (e.g. Railway, Render, Fly, or SSH + restart). Add any required secrets (e.g. `PROD_DEPLOY_SECRET`, API tokens) in repo Secrets.

See **docs/DEPLOY_OVERVIEW.md** for the full dev vs prod flow.
