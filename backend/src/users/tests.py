from ..tests import client


def test_create_user() -> None:
    response = client.post(
        "/users/",
        json={
            "username": "test",
            "password": "test",
        },
    )
    assert response.status_code == 200
    assert response.json() == {"username": "test"}


def test_read_users() -> None:
    response = client.get("/users")
    assert response.status_code == 200
    assert response.json() == []
