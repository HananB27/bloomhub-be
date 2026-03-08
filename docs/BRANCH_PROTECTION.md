# Branch protection (backend)

Same idea as the frontend repo:

1. **Settings** → **Branches** → Add rule for target branch (e.g. **Include default branch**).
2. **Require a pull request** with at least 1 approval.
3. **Require status checks** – add **CI** (from `.github/workflows/ci.yml`) after the first run.
4. **Restrict force push** as desired (e.g. disallow or restrict to admins).

See the frontend repo’s `docs/BRANCH_PROTECTION_SETUP.md` for the full step-by-step.
