import pytest

from fastapi.testclient import TestClient

from app.main import app


client = TestClient(app)


def test_root():

    response = client.get("/")

    assert response.status_code == 200
    assert response.json()["message"] == "Page Pulse API is running 🚀"


def test_valid_audit():

    response = client.post(
        "/audit",
        json={
            "url": "https://example.com"
        }
    )

    assert response.status_code == 200

    data = response.json()

    assert data["status"] == 200
    assert data["title"] == "Example Domain"


def test_invalid_url():

    response = client.post(
        "/audit",
        json={
            "url": "not-a-url"
        }
    )

    assert response.status_code == 422


def test_cache():

    url = "https://example.com"

    first = client.post(
        "/audit",
        json={"url": url}
    )

    second = client.post(
        "/audit",
        json={"url": url}
    )

    assert first.status_code == 200
    assert second.status_code == 200

    assert second.json()["cached"] is True
