from fastapi.testclient import TestClient

from backend.src.database import get_db
from backend.src.main import app
from tests.db import override_get_db

app.dependency_overrides[get_db] = override_get_db

client = TestClient(app)


def test_home():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {
        "message": "redoc - http://localhost:5000/redoc \n swagger - http://localhost:5000/docs"
    }
