def test_signup_login_and_me(client):
    signup_response = client.post(
        "/auth/signup", json={"email": "user@example.com", "password": "SecurePass123"}
    )
    assert signup_response.status_code == 201

    login_response = client.post(
        "/auth/login", json={"email": "user@example.com", "password": "SecurePass123"}
    )
    assert login_response.status_code == 200
    token = login_response.json()["access_token"]

    me_response = client.get("/auth/me", headers={"Authorization": f"Bearer {token}"})
    assert me_response.status_code == 200
    assert me_response.json()["email"] == "user@example.com"


def test_protected_route_requires_auth(client):
    response = client.get("/conversations")
    assert response.status_code == 403

