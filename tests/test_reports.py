from fastapi.testclient import TestClient

from src.api.main import app

client = TestClient(app)


def test_get_reports():
    response = client.get("/reports")

    assert response.status_code == 200

    data = response.json()

    assert isinstance(data, dict)
    assert "reports" in data