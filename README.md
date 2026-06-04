# AI-DLC Study Planner (DTS114TC Coursework)

AI-powered meta-software development coursework: one Jupyter Notebook generates SDLC artefacts, UML diagrams, a Flask API, a website with an AI dashboard image, tests, Docker configuration, and GitHub Actions CI.

## Repository structure

```text
Task1/
  AI_DLC_Study_Planner_Generator.ipynb
  generated_project/          # Flask app deployed for Task 2
Task2/
  deployment_notes.md
  screenshots/                # evidence images for submission zip
```

## Quick start (local)

```bash
cd Task1/generated_project
pip install -r requirements.txt
python -m pytest -q -p no:cacheprovider
python app/main.py
```

Open `http://127.0.0.1:5000`

## Task 2

- Public repository: version control and commit history on GitHub
- CI: `.github/workflows/ci.yml` runs `pytest` on push
- Deployment: see `Task2/deployment_notes.md`

API keys for LLM/image generation stay in `Task1/.env` (not committed).
