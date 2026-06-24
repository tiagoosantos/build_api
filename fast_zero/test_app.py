from fastapi.testclient import TestClient

from fast_zero.app import app

client = TestClient(app)


def test_read_root():
    """Testar o endpoint raiz."""
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello, World!"}
