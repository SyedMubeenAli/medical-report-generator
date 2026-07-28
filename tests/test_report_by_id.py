from fastapi.testclient import TestClient

from src.api.main import app

client = TestClient(app)


def test_get_report_by_valid_id():
    reports = client.get("/api/v1/reports").json()["reports"]

    assert len(reports) > 0

    report_id = reports[0]["report_id"]

    response = client.get(f"/api/v1/reports/{report_id}")

    assert response.status_code == 200

    data = response.json()

    assert data["patient"]["report_id"] == report_id


def test_get_report_by_invalid_id():
    response = client.get("/api/v1/reports/INVALID_ID")

    assert response.status_code == 404