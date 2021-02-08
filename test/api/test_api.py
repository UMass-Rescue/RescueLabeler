from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_read_main():
    """Sanity check test case. Load app and ping the home endpoint"""
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"msg": "RescueLab Labeler"}


def test_db():
    """Sanity check test case. Load app and ping the home endpoint"""
    response = client.get("/db_test/")
    assert response.status_code == 200
