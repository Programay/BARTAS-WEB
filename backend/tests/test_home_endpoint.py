from fastapi.testclient import TestClient

from src.main import app

client = TestClient(app)


def test_home():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {
        "message": "redoc - http://localhost:5000/redoc \n swagger - http://localhost:5000/docs"
    }
