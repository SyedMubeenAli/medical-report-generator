from fastapi.testclient import TestClient

from src.api.main import app

client = TestClient(app)


def test_get_reports():
    response = client.get("/api/v1/reports")

    assert response.status_code == 200

    data = response.json()

    assert isinstance(data, dict)

    assert "page" in data
    assert "limit" in data
    assert "total_reports" in data
    assert "total_pages" in data
    assert "reports" in data

    assert isinstance(data["reports"], list)