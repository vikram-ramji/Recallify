from ..app.main import app
from uuid import UUID

def test_signup(client):
    response = client.post("/auth/signup", json={
        "email": "test@example.com",
        "username": "testuser",
        "password": "strongpassword123",
        "password_confirm": "strongpassword123"
    })
    assert response.status_code == 200
    data = response.json()
    assert "access_token" in data
    assert "refresh_token" in response.cookies


def test_signin(client):
    # First, create the user
    client.post("/auth/signup", json={
        "email": "test2@example.com",
        "username": "testuser2",
        "password": "strongpassword123",
        "password_confirm": "strongpassword123"
    })

    # Then, test login
    response = client.post("/auth/signin", json={
        "email": "test2@example.com",
        "password": "strongpassword123"
    })

    assert response.status_code == 200
    data = response.json()
    assert "access_token" in data
