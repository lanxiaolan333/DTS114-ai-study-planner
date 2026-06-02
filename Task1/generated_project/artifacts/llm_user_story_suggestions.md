### User Story 1: Create a personalised weekly plan
**As a** student, **I want** to generate a weekly study plan from my course details, **so that** my independent study time is organised across modules.

**Acceptance Criteria**
- Given I provide **course name**, **difficulty level**, **available study hours/week**, **learning goal**, and **deadline**, when I click **Generate Plan**, then I see a **7-day schedule** with allocated study blocks.
- The plan distributes time across the week without exceeding my stated weekly hours.
- The plan includes at least: **module/topic**, **task type** (e.g., read, practice, revise), **estimated duration**, and **goal for the session**.
- If any required field is missing or invalid, the system prevents generation and shows a clear validation message.

---

### User Story 2: Balance workload by difficulty and deadline
**As a** student, **I want** the plan to adapt to difficulty and deadline proximity, **so that** I focus effort where it matters most.

**Acceptance Criteria**
- Given a **higher difficulty** selection, when a plan is generated, then a **greater proportion** of weekly hours is allocated to challenging modules/topics than for lower difficulty.
- Given a **nearer deadline**, when a plan is generated, then the plan schedules **more frequent sessions earlier in the week** and includes **revision buffers** before the deadline.
- The plan avoids scheduling all study hours in a single day unless my available hours require it.
- The generated plan clearly indicates the **deadline date** and how the plan leads up to it.

---

### User Story 3: Edit and regenerate without losing constraints
**As a** student, **I want** to adjust the plan and regenerate it, **so that** it fits changes in my availability or preferences.

**Acceptance Criteria**
- Given an existing plan, when I change available hours, goal, difficulty, or deadline and select **Regenerate**, then I receive an updated plan reflecting the new inputs.
- When I manually edit a study block (day/time/duration), the system prevents changes that exceed my total weekly hours and prompts me to resolve conflicts.
- The system provides a **Reset to AI plan** option that restores the latest generated version.
- Regeneration completes within an acceptable time (e.g., <10 seconds) or shows a loading state with progress feedback.

---

### User Story 4: Save and export the plan
**As a** student, **I want** to save and export my study plan, **so that** I can reuse it and follow it outside the app.

**Acceptance Criteria**
- Given a generated plan, when I click **Save**, then the plan is stored and accessible from a **My Plans** view.
- When I return later, I can open a saved plan and see the same schedule and inputs used to generate it.
- Given a saved or generated plan, when I click **Export**, then I can download it as **PDF or CSV** (at least one format required).
- Exported content includes: course name, week overview, daily blocks, and total hours/week.
