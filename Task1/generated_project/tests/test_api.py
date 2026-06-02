import json
import pytest
from app.main import app


@pytest.fixture()
def client():
    app.config.update(TESTING=True)
    with app.test_client() as test_client:
        yield test_client


def test_health_check(client):
    response = client.get("/health")
    assert response.status_code == 200
    assert response.get_json()["status"] == "ok"


def test_sample_plan(client):
    response = client.get("/api/sample-plan")
    data = response.get_json()
    assert response.status_code == 200
    assert data["course_name"]
    assert len(data["weekly_plan"]) == 7


def test_create_plan_success(client):
    payload = {
        "course_name": "DTS114TC AI Software Engineering",
        "difficulty": "hard",
        "available_hours": 8,
        "learning_goal": "prepare coursework and deployment evidence",
        "deadline": "2026-06-07",
    }
    response = client.post("/api/plan", data=json.dumps(payload), content_type="application/json")
    data = response.get_json()
    assert response.status_code == 201
    assert data["difficulty"] == "hard"
    assert len(data["weekly_plan"]) == 7
    assert "revision_advice" in data


def test_create_plan_validation_error(client):
    response = client.post("/api/plan", json={"course_name": "DTS114TC"})
    data = response.get_json()
    assert response.status_code == 400
    assert data["error"] == "missing_required_fields"
