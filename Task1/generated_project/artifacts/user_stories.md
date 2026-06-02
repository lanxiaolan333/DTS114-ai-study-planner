## User Stories

### Story 1: Student
As a Student, I want to generate a weekly study plan from my course details, so that I can organise study time more effectively.

Acceptance criteria:
- Given valid inputs, when I submit the form, then the system returns a weekly plan.
- The response includes daily tasks, estimated hours, revision advice, and risk flags.

### Story 2: Student
As a Student, I want to see a sample plan before entering my own information, so that I can understand what the system produces.

Acceptance criteria:
- GET /api/sample-plan returns a valid example plan.
- The example contains the same structure as a generated plan.

### Story 3: Developer
As a Developer, I want to check the health of the deployed API, so that I can verify that deployment is working.

Acceptance criteria:
- GET /health returns status ok.
- The response uses JSON and HTTP 200.

### Story 4: Developer
As a Developer, I want to run automated tests before deployment, so that I reduce the risk of releasing broken code.

Acceptance criteria:
- The project includes pytest tests.
- GitHub Actions runs the tests on push.
