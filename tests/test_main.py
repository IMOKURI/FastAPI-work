from fastapi.testclient import TestClient

from app import app

client = TestClient(app)


def test_read_sync():
    response = client.get("/sync")
    assert response.status_code == 200
    assert response.json() == {"Hello": "Common"}
