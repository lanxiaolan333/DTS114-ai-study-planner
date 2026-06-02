## RESTful Flask API Endpoint Design

### 1) `GET /`
**Purpose:** Serve the web application entry point (UI) or basic landing content.

- **Auth:** None
- **Request:** No body
- **Response (200 OK):**
  - **Content-Type:** `text/html; charset=utf-8`
  - **Body:** HTML page (e.g., rendered template `index.html`)
- **Errors:**
  - `500 Internal Server Error` (unexpected server failure)

---

### 2) `GET /health`
**Purpose:** Liveness/health probe for monitoring and deployment platforms.

- **Auth:** None
- **Request:** No body
- **Response (200 OK):**
  - **Content-Type:** `application/json`
  - **Body (example):**
    ```json
    {
      "status": "ok",
      "service": "ai-dlc-planner",
      "version": "1.0.0",
      "time": "2026-06-02T12:34:56Z"
    }
    ```
- **Errors:**
  - `503 Service Unavailable` if a required dependency check fails (optional design)
  - **Body (example):**
    ```json
    { "status": "degraded", "reason": "model_unavailable" }
    ```

---

### 3) `GET /api/sample-plan`
**Purpose:** Return a deterministic sample plan structure for UI scaffolding/testing.

- **Auth:** None (or optional API key if required by course)
- **Request:** No body
- **Response (200 OK):**
  - **Content-Type:** `application/json`
  - **Body (example):**
    ```json
    {
      "plan_id": "sample",
      "title": "AI-DLC Sample Plan",
      "inputs": {
        "goal": "Build a Flask-based AI planning API",
        "constraints": ["2 weeks", "single developer", "basic ML integration"]
      },
      "phases": [
        {
          "name": "Requirements",
          "tasks": [
            { "id": "R1", "task": "Define scope and user stories", "deliverable": "Requirements doc" },
            { "id": "R2", "task": "Identify risks and assumptions", "deliverable": "Risk register" }
          ]
        },
        {
          "name": "Design",
          "tasks": [
            { "id": "D1", "task": "API contract + data models", "deliverable": "OpenAPI draft" },
            { "id": "D2", "task": "Architecture + components", "deliverable": "Architecture diagram" }
          ]
        },
        {
          "name": "Implementation",
          "tasks": [
            { "id": "I1", "task": "Flask endpoints + validation", "deliverable": "Working API" },
            { "id": "I2", "task": "Model integration stub", "deliverable": "Planner module" }
          ]
        },
        {
          "name": "Testing",
          "tasks": [
            { "id": "T1", "task": "Unit tests for endpoints", "deliverable": "pytest suite" },
            { "id": "T2", "task": "Contract tests for JSON schema", "deliverable": "schema tests" }
          ]
        }
      ]
    }
    ```
- **Errors:**
  - `500 Internal Server Error` (unexpected server failure)

---

### 4) `POST /api/plan`
**Purpose:** Generate a plan from user inputs (optionally using an LLM/AI module). Returns a structured plan.

- **Auth:** Optional (Bearer token / API key). If used:
  - **Header:** `Authorization: Bearer <token>`
  - **Errors:** `401 Unauthorized`, `403 Forbidden`

#### Request
- **Content-Type:** `application/json`
- **Body (example):**
  ```json
  {
    "goal": "Create an AI-driven DLC study plan for a Flask project",
    "context": "Coursework project using Flask + REST API + basic AI module",
    "constraints": ["7 days", "2-person team", "no paid APIs"],
    "audience": "Undergraduate CS",
    "deliverables": ["API endpoints", "tests", "report"],
    "preferences": {
      "detail_level": "medium",
      "include_risks": true,
      "include_milestones": true
    }
  }
  ```

#### Request Fields (recommended contract)
- `goal` *(string, required, 1–500 chars)*: Primary objective.
- `context` *(string, optional)*: Background/problem domain.
- `constraints` *(array[string], optional)*: Time/budget/tech constraints.
- `audience` *(string, optional)*: Intended readership.
- `deliverables` *(array[string], optional)*: Expected outputs.
- `preferences` *(object, optional)*:
  - `detail_level` *(string, optional: "low"|"medium"|"high")*
  - `include_risks` *(boolean, optional)*
  - `include_milestones` *(boolean, optional)*

#### Successful Response
- **Status:** `201 Created` (preferred) or `200 OK`
- **Headers:**
  - `Content-Type: application/json`
  - `Location: /api/plan/<plan_id>` *(optional if you later implement retrieval)*
- **Body (example):**
  ```json
  {
    "plan_id": "pln_7f3a2c",
    "title": "AI-DLC Plan: Flask Coursework",
    "generated_at": "2026-06-02T12:34:56Z",
    "inputs": {
      "goal": "Create an AI-driven DLC study plan for a Flask project",
      "constraints": ["7 days", "2-person team", "no paid APIs"]
    },
    "milestones": [
      { "name": "API Contract Finalized", "due_day": 1 },
      { "name": "Core Endpoints Implemented", "due_day": 3 },
      { "name": "Tests + Report Draft", "due_day": 6 },
      { "name": "Submission Ready", "due_day": 7 }
    ],
    "phases": [
      {
        "name": "Requirements",
        "tasks": [
          {
            "id": "R1",
            "task": "Write user stories and acceptance criteria",
            "estimated_hours": 2,
            "outputs": ["requirements.md"]
          }
        ]
      },
      {
        "name": "Design",
        "tasks": [
          {
            "id": "D1",
            "task": "Define JSON schema for /api/plan and /api/sample-plan",
            "estimated_hours": 2,
            "outputs": ["openapi.yaml", "schemas/plan.json"]
          }
        ]
      },
      {
        "name": "Implementation",
        "tasks": [
          {
            "id": "I1",
            "task": "Implement Flask routes + input validation",
            "estimated_hours": 4,
            "outputs": ["app.py", "planner.py"]
          }
        ]
      },
      {
        "name": "Testing",
        "tasks": [
          {
            "id": "T1",
            "task": "Add pytest unit + integration tests",
            "estimated_hours": 4,
            "outputs": ["tests/test_api.py"]
          }
        ]
      }
    ],
    "risks": [
      { "risk": "Scope creep", "mitigation": "Lock deliverables on day 1" },
      { "risk": "Model output inconsistency", "mitigation": "Enforce JSON schema + retries" }
    ]
  }
  ```

#### Error Responses
- **400 Bad Request** (invalid JSON, missing `goal`, schema violations)
  - **Body (example):**
    ```json
    {
      "error": "validation_error",
      "message": "Field 'goal' is required",
      "details": { "goal": ["missing"] }
    }
    ```
- **415 Unsupported Media Type** (non-JSON request)
  - **Body:**
    ```json
    { "error": "unsupported_media_type", "message": "Use Content-Type: application/json" }
    ```
- **422 Unprocessable Entity** (well-formed JSON but semantically invalid; optional distinction from 400)
  - **Body:**
    ```json
    { "error": "unprocessable_entity", "message": "constraints must be an array of strings" }
    ```
- **500 Internal Server Error** (unexpected)
  - **Body:**
    ```json
    { "error": "server_error", "message": "Unexpected error occurred" }
    ```
- **503 Service Unavailable** (AI/model dependency unavailable; recommended if using external model)
  - **Body:**
    ```json
    { "error": "service_unavailable", "message": "Planner model unavailable, try again later" }
    ```

---

## Common API Conventions (applies to `/api/*`)
- **All JSON responses:** `Content-Type: application/json`
- **Traceability (optional):** include `X-Request-ID` header and echo in responses.
- **CORS (optional for UI):** allow `GET, POST` to `/api/*`.
- **Rate limiting (optional):** return `429 Too Many Requests` with:
  ```json
  { "error": "rate_limited", "message": "Too many requests" }
  ```
