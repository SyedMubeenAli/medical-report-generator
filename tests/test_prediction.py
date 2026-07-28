from fastapi.testclient import TestClient

from src.api.main import app

client = TestClient(app)


VALID_PAYLOAD = {
    "Age": 35,
    "Gender": "Male",
    "Hemoglobin": 14.2,
    "WBC": 7200,
    "RBC": 5.1,
    "Platelets": 250000,
    "Hematocrit": 42,
    "MCV": 90.5,
    "MCH": 30.2,
    "MCHC": 33.5,
}


def test_prediction_success():
    response = client.post(
        "/api/v1/reports/analyze",
        json=VALID_PAYLOAD,
    )

    assert response.status_code == 200

    data = response.json()

    assert "prediction" in data
    assert "confidence" in data
    assert "severity" in data
    assert "summary" in data
    assert "recommendation" in data


def test_prediction_validation():
    invalid_payload = VALID_PAYLOAD.copy()
    invalid_payload["Age"] = -5

    response = client.post(
        "/api/v1/reports/analyze",
        json=invalid_payload,
    )

    assert response.status_code == 422