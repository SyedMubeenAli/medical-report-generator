from fastapi.testclient import TestClient

from src.api.main import app

client = TestClient(app)


def test_get_report_by_id():
    reports = client.get("/reports").json()["reports"]

    if not reports:
        return

    report_id = reports[0]["report_id"]

    response = client.get(f"/reports/{report_id}")

    assert response.status_code == 200

    data = response.json()

    assert data["patient"]["report_id"] == report_id