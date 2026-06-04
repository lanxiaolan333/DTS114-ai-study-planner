## Functional Requirements (FR)

### FR1 — User Access & Navigation
- The website shall provide a landing page explaining the AI Study Planner and how to use it.
- The website shall allow users to access the planner without requiring account registration (guest mode).
- The website shall provide navigation to: planner form, generated plan view, and help/about content.

### FR2 — Study Plan Input Collection
- The website shall provide a form to capture the following inputs:
  - Course name (text)
  - Difficulty level (predefined options, e.g., Easy/Medium/Hard)
  - Available study hours per week (numeric)
  - Learning goal (text or predefined options)
  - Deadline (date)
- The system shall validate inputs (required fields, numeric ranges, valid date) before generating a plan.
- The system shall display clear validation errors when inputs are invalid.

### FR3 — Plan Generation (AI)
- The Flask API shall expose an endpoint to generate a study plan from the provided inputs.
- The system shall use an AI component to generate a personalised weekly study plan.
- The generated plan shall allocate study time across the week and align activities with the learning goal and deadline.
- The system shall include module/course context (course name and difficulty) in the generated plan.

### FR4 — Plan Output & Presentation
- The website shall display the generated plan in a readable weekly schedule format (e.g., day-by-day breakdown).
- The output shall include:
  - Total planned study hours for the week
  - Daily tasks/activities
  - Milestones aligned to the deadline
- The system shall allow users to regenerate a plan with adjusted inputs.

### FR5 — Plan Management (Session-Based)
- The system shall store the most recently generated plan for the current user session.
- The website shall allow users to view the most recent plan without re-entering inputs during the same session.
- The system shall allow users to clear/reset the current session plan.

### FR6 — Export/Download
- The website shall allow users to export the generated plan as a downloadable file (e.g., PDF or CSV).
- The Flask API shall provide an endpoint that returns the plan export in the chosen format.

### FR7 — API Design & Responses
- The Flask API shall return responses in JSON for all API endpoints.
- The API shall return appropriate HTTP status codes (e.g., 200, 400, 500) and error messages for failures.
- The API shall provide a health check endpoint for monitoring availability.

### FR8 — Help & Guidance
- The website shall provide brief guidance on how to enter inputs and interpret the generated plan.
- The system shall display user-friendly error pages/messages when plan generation fails.

---

## Non-Functional Requirements (NFR)

### NFR1 — Usability & Accessibility
- The website shall be usable on modern desktop and mobile browsers (responsive layout).
- The interface shall be simple enough to complete plan generation within 2 minutes for a first-time user.
- The website shall meet basic accessibility expectations (e.g., semantic HTML, form labels, keyboard navigation).

### NFR2 — Performance
- The API shall respond to plan generation requests within an acceptable time (target: ≤ 10 seconds under normal load).
- The website shall load primary pages within an acceptable time (target: ≤ 3 seconds on typical broadband).

### NFR3 — Reliability & Availability
- The system shall handle invalid input and AI errors gracefully without crashing.
- The API shall maintain consistent availability during expected usage hours (target: 99% uptime for coursework deployment).
- The system shall provide meaningful fallback error messages if the AI service is unavailable.

### NFR4 — Security
- The system shall validate and sanitise all user inputs server-side.
- The API shall implement protection against common web vulnerabilities (e.g., XSS, CSRF for form posts where applicable).
- The system shall not log sensitive user-provided free-text content unnecessarily.

### NFR5 — Privacy & Data Protection
- The system shall minimise stored personal data; guest mode shall not require personally identifiable information.
- Session data (if used) shall be stored securely and cleared after a defined period of inactivity.

### NFR6 — Maintainability
- The codebase shall follow a clear project structure (routes/controllers, services, templates, static assets).
- The system shall separate AI plan generation logic from Flask route handling.
- The project shall include inline documentation and a README describing setup and usage.

### NFR7 — Testability
- The system shall include automated tests for input validation and API responses (unit/integration tests).
- The plan generation component shall be testable using mocked AI responses.

### NFR8 — Portability & Deployment
- The application shall be deployable on a standard WSGI-compatible environment (e.g., Gunicorn).
- The project shall use dependency management (e.g., `environment.yml`) and configurable environment variables for secrets/keys.

### NFR9 — Observability & Logging
- The system shall log key events (requests, errors) with timestamps for troubleshooting.
- The API shall include structured error responses to support debugging and client-side handling.
