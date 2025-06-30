from app.main import app
from uuid import UUID

def test_create_user(client):
    response = client.post("/users/", json={
        "email": "test_create@example.com"
    })
    assert response.status_code == 200
    assert response.json()["email"] == "test_create@example.com"

def test_get_user(client):
    response = client.post("/users/", json={
        "email": "test_get@example.com"
    })
    assert response.status_code == 200
    user_id = UUID(response.json()["id"])

    user = client.get(f"/users/{user_id}")
    print(f"user_id : {user_id}")
    assert user.status_code == 200
    assert user.json()["email"] == "test_get@example.com"