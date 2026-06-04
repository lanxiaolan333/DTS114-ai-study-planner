# AI Usage Log

This file records the AI-specific tooling used by the notebook (APIFree LLM and image API via prompts in `AI_DLC_Study_Planner_Generator.ipynb`). GitHub Copilot was not used. API keys are loaded from `Task1/.env` and are never written into generated artefacts.

- Provider: apifree
- Text model: openai/gpt-5.2
- Image model: openai/gpt-image-2

## Prompts

- **problem_statement**: Generate one concise problem statement for this business problem:
Students often struggle to organise independent study time across multiple modules.
They need a web-based AI Study Planner that generates a personalised weekly study plan
based on course name, difficulty level, available study hours, learning goal, and deadline.
- **personas**: Generate 3 concise personas for this system. Use markdown and include responsibilities and needs.
Business problem:
Students often struggle to organise independent study time across multiple modules.
They need a web-based AI Study Planner that generates a personalised weekly study plan
based on course name, difficulty level, available study hours, learning goal, and deadline.
- **requirements**: Generate functional and non-functional requirements for a Flask API and website. Use markdown headings.
Business problem:
Students often struggle to organise independent study time across multiple modules.
They need a web-based AI Study Planner that generates a personalised weekly study plan
based on course name, difficulty level, available study hours, learning goal, and deadline.
- **user_stories**: Generate 4 user stories with acceptance criteria for an AI Study Planner. Use concise markdown.
Business problem:
Students often struggle to organise independent study time across multiple modules.
They need a web-based AI Study Planner that generates a personalised weekly study plan
based on course name, difficulty level, available study hours, learning goal, and deadline.
- **api_endpoints**: Design RESTful Flask API endpoints for GET /, GET /health, GET /api/sample-plan, and POST /api/plan. Include request and response details.
- **uml_use_case**: Generate only valid PlantUML for a use case diagram. Actor Student uses the AI Study Planner to enter course, difficulty, available hours, learning goal, and deadline; generate a weekly plan; and view a sample plan. Actor Developer checks API health.
- **uml_component**: Generate only valid PlantUML for a component diagram with Student, Web Interface, Flask API, StudyPlanGenerator, and JSON Study Plan.
- **uml_sequence**: Generate only valid PlantUML for a sequence diagram showing Student submitting study inputs and the Flask API returning a weekly plan.
- **website**: Generate a website that displays an automatically generated image and calls POST /api/plan.
- **tests**: Generate pytest tests for health, sample plan, successful plan, and validation errors.

## Call Results

- **problem_statement**: api (openai/gpt-5.2)
- **personas**: api (openai/gpt-5.2)
- **requirements**: api (openai/gpt-5.2)
- **api_endpoints**: api (openai/gpt-5.2)
- **user_stories_markdown**: api (openai/gpt-5.2)
- **uml_use_case**: api (openai/gpt-5.2)
- **uml_component**: api (openai/gpt-5.2)
- **uml_sequence**: api (openai/gpt-5.2)
- **ai_study_image**: api (openai/gpt-image-2)
