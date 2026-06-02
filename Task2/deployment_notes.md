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

Recommended Render settings:

- Root directory: `Task1/generated_project`
- Build command: `pip install -r requirements.txt`
- Start command: `gunicorn app.main:app`

After deployment, capture the deployed website page showing the AI-generated dashboard image and the study planner form.

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

