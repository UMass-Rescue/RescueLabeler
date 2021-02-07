from fastapi.testclient import TestClient
from labeler_api.main import app

client = TestClient(app)


def test_read_main():
    """Sanity check test case. Load app and ping the home endpoint"""
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"msg": "RescueLab Labeler"}
