# 🤖 **AI Chatbot API**

[![FastAPI](https://img.shields.io/badge/FastAPI-0.115-05998b?logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com/)
[![PostgreSQL](https://img.shields.io/badge/PostgreSQL-16-316192?logo=postgresql&logoColor=white)](https://postgresql.org/)
[![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-2.0-red?logo=sqlalchemy&logoColor=white)](https://www.sqlalchemy.org/)
[![Alembic](https://img.shields.io/badge/Alembic-Migrations-black)](https://alembic.sqlalchemy.org/)
[![Docker](https://img.shields.io/badge/Docker-24.0-2496ED?logo=docker&logoColor=white)](https://docker.com/)

Production-grade **FastAPI** backend for a conversation-aware AI assistant. Built with **PostgreSQL**, **SQLAlchemy 2.0**, **Alembic**, **JWT auth**, and **OpenAI** integration. Clean separation of concerns, typed IO, and deployment-ready Docker setup.

> ✅ **JWT Auth** · 🧠 **LLM Integration** · 🐳 **Dockerized** · 🧪 **Tested**

---

## 📌 **Table of Contents**
- [✨ Overview](#-overview)
- [🏗️ Architecture](#️-architecture)
- [🔐 Auth Endpoints](#-auth-endpoints)
- [💬 Chat Endpoints](#-chat-endpoints)
- [🧪 Example Request](#-example-request)
- [⚙️ Environment](#️-environment)
- [🚀 Local Setup](#-local-setup)
- [🐳 Docker Setup](#-docker-setup)
- [🧪 Testing](#-testing)
- [📈 Portfolio Value](#-portfolio-value)

---

## ✨ **Overview**
This API powers a professional AI chat experience with secure user authentication, persistent conversations, and LLM-backed responses. It’s designed to be scalable, predictable, and easy to deploy.

---

## 🏗️ **Architecture**
- `app/main.py`: FastAPI app + middleware
- `app/config.py`: environment configuration
- `app/database.py`: SQLAlchemy engine/session
- `app/models/`: `User`, `Conversation`, `Message`
- `app/schemas/`: request/response DTOs
- `app/routers/`: `/auth`, `/chat`, `/conversations`
- `app/services/llm.py`: OpenAI chat completions
- `app/utils/jwt.py`: password hashing + JWT helpers
- `alembic/`: migration tooling

---

## 🔐 **Auth Endpoints**
```
POST /auth/signup
POST /auth/login
GET  /auth/me
```

---

## 💬 **Chat Endpoints**
```
POST /chat
GET  /conversations
GET  /conversations/{id}
```

---

## 🧪 **Example Request**
```json
{
  "message": "Hello",
  "conversation_id": null
}
```

Response:
```json
{
  "conversation_id": "3e4b6c8d-7c60-4e4c-9d24-4bfc4d1d2f3b",
  "reply": "AI response here"
}
```

---

## ⚙️ **Environment**
Create `.env` from `.env.example`:
```env
DATABASE_URL=postgresql+psycopg2://ai_user:ai_password@localhost:5432/ai_chatbot
JWT_SECRET_KEY=change_me
JWT_ALGORITHM=HS256
JWT_EXPIRE_MINUTES=30
OPENAI_API_KEY=
```

---

## 🚀 **Local Setup**
```bash
pip install -r requirements.txt
alembic upgrade head
uvicorn app.main:app --reload
```

---

## 🐳 **Docker Setup**
```bash
docker-compose up --build
```

---

## 🧪 **Testing**
```bash
pytest
```

---

## 📈 **Portfolio Value**
- Clean separation of concerns and typed IO models
- Secure JWT authentication with bcrypt hashing
- Conversation persistence and AI memory
- Production-ready Docker + Alembic migrations

