from datetime import datetime
import os
from flask import Flask, jsonify, render_template, request
from flask_cors import CORS


def create_app():
    app = Flask(__name__, template_folder="templates", static_folder="static")
    CORS(app)

    @app.get("/")
    def home():
        return render_template("index.html")

    @app.get("/health")
    def health():
        return jsonify({"status": "ok", "service": "ai-study-planner"}), 200

    @app.get("/api/sample-plan")
    def sample_plan():
        plan = generate_plan(
            course_name="DTS114TC AI Software Engineering",
            difficulty="hard",
            available_hours=8,
            learning_goal="prepare coursework evidence and final revision",
            deadline="2026-06-07",
        )
        return jsonify(plan), 200

    @app.post("/api/plan")
    def create_plan():
        data = request.get_json(silent=True) or {}
        required = ["course_name", "difficulty", "available_hours", "learning_goal", "deadline"]
        missing = [field for field in required if data.get(field) in (None, "")]
        if missing:
            return jsonify({"error": "missing_required_fields", "fields": missing}), 400
        try:
            available_hours = float(data["available_hours"])
        except (TypeError, ValueError):
            return jsonify({"error": "available_hours_must_be_a_number"}), 400
        if available_hours <= 0:
            return jsonify({"error": "available_hours_must_be_positive"}), 400
        difficulty = str(data["difficulty"]).lower().strip()
        if difficulty not in {"easy", "medium", "hard"}:
            return jsonify({"error": "difficulty_must_be_easy_medium_or_hard"}), 400
        plan = generate_plan(
            course_name=str(data["course_name"]).strip(),
            difficulty=difficulty,
            available_hours=available_hours,
            learning_goal=str(data["learning_goal"]).strip(),
            deadline=str(data["deadline"]).strip(),
        )
        return jsonify(plan), 201

    return app


def generate_plan(course_name, difficulty, available_hours, learning_goal, deadline):
    multiplier = {"easy": 0.85, "medium": 1.0, "hard": 1.25}[difficulty]
    effective_hours = round(available_hours * multiplier, 1)
    daily_hours = distribute_hours(effective_hours)
    focus_path = build_focus_path(course_name, learning_goal, difficulty)
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    weekly_plan = []
    for index, day in enumerate(days):
        topic = focus_path[index % len(focus_path)]
        task_type = "Review and summarise" if index in {0, 3} else "Practice and produce evidence"
        if day == "Sunday":
            task_type = "Reflect, test knowledge, and adjust next week"
        weekly_plan.append({
            "day": day,
            "topic": topic,
            "task": f"{task_type}: {topic}",
            "estimated_hours": daily_hours[index],
        })
    risk_flags = []
    if available_hours < 5 and difficulty in {"medium", "hard"}:
        risk_flags.append("Available hours may be too low for the selected difficulty.")
    if not looks_like_date(deadline):
        risk_flags.append("Deadline format was not recognised; use YYYY-MM-DD for clearer planning.")
    if not risk_flags:
        risk_flags.append("Plan is feasible if tasks are completed consistently.")
    return {
        "course_name": course_name,
        "difficulty": difficulty,
        "available_hours": available_hours,
        "learning_goal": learning_goal,
        "deadline": deadline,
        "weekly_plan": weekly_plan,
        "revision_advice": build_revision_advice(difficulty, available_hours),
        "risk_flags": risk_flags,
        "generated_by": "AI-DLC Study Planner Generator",
    }


def distribute_hours(total_hours):
    weights = [0.15, 0.15, 0.15, 0.15, 0.17, 0.15, 0.08]
    hours = [round(total_hours * weight, 1) for weight in weights]
    hours[-1] = round(hours[-1] + round(total_hours - sum(hours), 1), 1)
    return hours


def build_focus_path(course_name, learning_goal, difficulty):
    base = [
        "Clarify requirements and success criteria",
        "Review core concepts and lecture notes",
        "Create examples or diagrams",
        "Practise implementation tasks",
        "Run tests and fix weak areas",
        "Prepare submission evidence",
        "Reflect and plan improvements",
    ]
    if "software" in course_name.lower() or "api" in learning_goal.lower():
        base[2] = "Model architecture with UML"
        base[3] = "Implement API and website tasks"
        base[4] = "Run pytest and deployment checks"
    if difficulty == "hard":
        base.insert(4, "Reserve extra time for debugging and revision")
    return base


def build_revision_advice(difficulty, available_hours):
    if difficulty == "hard":
        return "Use short daily sessions, test yourself twice, and reserve time for debugging or rework."
    if available_hours >= 8:
        return "Use a balanced plan with concept review, active recall, and practical output."
    return "Prioritise the highest-value topics and keep each task small enough to finish."


def looks_like_date(value):
    try:
        datetime.strptime(value, "%Y-%m-%d")
        return True
    except ValueError:
        return False


app = create_app()

if __name__ == "__main__":
    port = int(os.environ.get("PORT", "5000"))
    app.run(host="0.0.0.0", port=port, debug=False)
