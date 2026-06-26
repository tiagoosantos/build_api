import pytest
from fastapi.testclient import TestClient

from fast_zero.app import app, database

client = TestClient(app)


@pytest.fixture(autouse=True)
def clear_database():
    database.clear()


def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello, World!"}


def test_create_user():
    response = client.post(
        "/users",
        json={
            "username": "alice",
            "email": "alice@example.com",
            "password": "secret123",
        },
    )

    assert response.status_code == 201
    assert response.json() == {
        "id": 1,
        "username": "alice",
        "email": "alice@example.com",
    }


