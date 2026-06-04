# Task2 Deployment Notes

## Version Control Evidence

Screenshot required:

- `Task2/screenshots/01_commit_records.png`

Capture the GitHub commit history page after pushing the repository.

## CI/CD Evidence

Screenshot required:

- `Task2/screenshots/03_cicd_workflow.png`

Capture the GitHub Actions `CI` workflow page after it passes successfully.

## Deployment Evidence

Screenshot required:

- `Task2/screenshots/02_website_deployment.png`

After deployment, capture the deployed website page showing the AI-generated dashboard image and the study planner form.

### Railway (recommended)

1. [railway.app](https://railway.app) → **New Project** → deploy from this GitHub repository.
2. **Root Directory**: `Task1/generated_project`
3. Uses existing `Dockerfile` (`gunicorn app.main:app`) or set **Start Command**: `gunicorn app.main:app --bind 0.0.0.0:$PORT`
4. **Generate Domain** for a public `https://` URL.
5. No `APIFREE_API_KEY` required at runtime (static image is in `app/static/`).

### Render (alternative)

- Root directory: `Task1/generated_project`
- Build command: `pip install -r requirements.txt`
- Start command: `gunicorn app.main:app`

### PythonAnywhere (alternative)

Configure WSGI to import `application` from `app.main` in `Task1/generated_project`.

## Local Verification Commands

Run from `Task1/generated_project`:

```bash
python -m pytest -q -p no:cacheprovider
python app/main.py
```

Open:

```text
http://127.0.0.1:5000
```

