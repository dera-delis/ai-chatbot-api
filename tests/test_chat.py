from app.routers import chat


def _auth_token(client):
    client.post("/auth/signup", json={"email": "chat@example.com", "password": "SecurePass123"})
    login_response = client.post(
        "/auth/login", json={"email": "chat@example.com", "password": "SecurePass123"}
    )
    return login_response.json()["access_token"]


def test_chat_flow_creates_conversation_and_messages(client, monkeypatch):
    token = _auth_token(client)

    def fake_reply(messages):
        assert messages[-1]["role"] == "user"
        return "Mocked response"

    monkeypatch.setattr(chat, "generate_reply", fake_reply)

    chat_response = client.post(
        "/chat",
        json={"message": "Hello", "conversation_id": None},
        headers={"Authorization": f"Bearer {token}"},
    )
    assert chat_response.status_code == 200
    payload = chat_response.json()
    conversation_id = payload["conversation_id"]
    assert payload["reply"] == "Mocked response"

    list_response = client.get("/conversations", headers={"Authorization": f"Bearer {token}"})
    assert list_response.status_code == 200
    assert any(conv["id"] == conversation_id for conv in list_response.json())

    detail_response = client.get(
        f"/conversations/{conversation_id}", headers={"Authorization": f"Bearer {token}"}
    )
    assert detail_response.status_code == 200
    messages = detail_response.json()["messages"]
    assert len(messages) == 2
    assert messages[0]["role"] == "user"
    assert messages[1]["role"] == "assistant"

