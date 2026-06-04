# Task2 Deployment Notes

## Version Control Evidence

Screenshot required:

- `Task2/screenshots/01_commit_records.png`

Capture the GitHub commit history page after pushing the repository.

## CI/CD Evidence

Screenshot required:

- `Task2/screenshots/03_cicd_workflow.png`

Capture the GitHub Actions `CI` workflow page after it passes successfully.

## Deployment Evidence (GitHub Pages)

Screenshot required:

- `Task2/screenshots/02_website_deployment.png`

### One-time GitHub setting

1. Open repository **Settings** → **Pages**.
2. Under **Build and deployment**, set **Source** to **GitHub Actions**.

### Automatic deployment

Workflow: `.github/workflows/pages.yml`

- Deploys the static site from the `docs/` folder on each push to `main`.
- Public URL format:

```text
https://lanxiaolan333.github.io/DTS114-ai-study-planner/
```

### What is deployed

| Location | Role |
|----------|------|
| `docs/` | GitHub Pages website (HTML + AI dashboard image + client-side plan generator) |
| `Task1/generated_project/` | Flask API source used locally and tested by CI (`pytest`) |

GitHub Pages hosts static files only. The deployed site uses the same study-plan logic as the Flask app, implemented in browser JavaScript. The Flask API remains in the repository for Task 1 evidence and automated testing.

Capture the live Pages URL showing the AI-generated dashboard image and the study planner form.

## Local Flask verification

From the repository root, use `environment.yml` (see root `README.md`), then run from `Task1/generated_project`:

```bash
conda activate ai_in_se_chapter_04
python -m pytest -q -p no:cacheprovider
python app/main.py
```

Open:

```text
http://127.0.0.1:5000
```
