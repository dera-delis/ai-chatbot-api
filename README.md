# AI Chatbot API

Production-ready FastAPI backend for an authenticated, conversation-based AI chatbot. Built for real-world deployment with PostgreSQL, SQLAlchemy 2.0, Alembic, JWT auth, and OpenAI integration.

## Architecture
- `app/main.py`: FastAPI application entrypoint
- `app/config.py`: environment-driven settings
- `app/database.py`: SQLAlchemy engine/session + dependency
- `app/models/`: SQLAlchemy models (`User`, `Conversation`, `Message`)
- `app/schemas/`: Pydantic request/response models
- `app/routers/`: API routes (`/auth`, `/chat`, `/conversations`)
- `app/services/llm.py`: OpenAI chat completion integration
- `app/utils/jwt.py`: JWT + password hashing utilities
- `alembic/`: migration configuration

## API Endpoints

Auth
- `POST /auth/signup`
- `POST /auth/login`
- `GET /auth/me`

Chat
- `POST /chat`
- `GET /conversations`
- `GET /conversations/{id}`

## Example Request/Response

Request:
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

## Local Setup
1. Create `.env` from `.env.example`
2. Install dependencies:
   - `pip install -r requirements.txt`
3. Run migrations:
   - `alembic upgrade head`
4. Start API:
   - `uvicorn app.main:app --reload`

## Docker Setup
1. Create `.env` from `.env.example`
2. Run:
   - `docker-compose up --build`

## Testing
- `pytest`

## Portfolio Value
- Clean separation of concerns, secure JWT authentication, and SQLAlchemy 2.0 patterns
- Production-grade logging, migrations, and Dockerized deployment
- Scalable chat architecture with conversation history and LLM integration

