from fastapi.testclient import TestClient

from src.api.main import app

client = TestClient(app)


def get_report_id():
    response = client.get("/api/v1/reports")

    assert response.status_code == 200

    reports = response.json()["reports"]

    assert len(reports) > 0

    return reports[0]["report_id"]


def test_update_report():
    report_id = get_report_id()

    payload = {
        "patient_name": "Updated Test Patient",
        "age": 30,
        "gender": "Male",
        "condition": "Healthy",
        "severity": "Normal"
    }

    response = client.put(
        f"/api/v1/reports/{report_id}",
        json=payload
    )

    assert response.status_code == 200

    data = response.json()

    assert data["patient"]["name"] == "Updated Test Patient"
    assert data["patient"]["age"] == 30


def test_delete_invalid_report():
    response = client.delete(
        "/api/v1/reports/INVALID_ID"
    )

    assert response.status_code == 404