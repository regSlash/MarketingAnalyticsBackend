from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_analytics_endpoint():
    response = client.get(
        "/api/analytics",
        headers={"X-API-Key": "secure-key-123"}
    )
    assert response.status_code == 200
    assert 'instantly' in response.json()