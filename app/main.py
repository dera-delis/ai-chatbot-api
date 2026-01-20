import logging
import os
import sys

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routers import auth, chat


logging.basicConfig(
    level=logging.INFO,
    stream=sys.stdout,
    format="%(asctime)s %(levelname)s %(name)s %(message)s",
)

app = FastAPI(title="AI Chatbot API", version="1.0.0")

cors_env = os.getenv("CORS_ORIGINS")
default_origins = [
    "http://localhost:3000",
    "http://127.0.0.1:3000",
    "https://ai-chatbot-app-three.vercel.app",
]
allow_origins = [origin.strip() for origin in cors_env.split(",")] if cors_env else default_origins

app.add_middleware(
    CORSMiddleware,
    allow_origins=allow_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth.router)
app.include_router(chat.router)


@app.get("/health", tags=["health"])
def health_check() -> dict[str, str]:
    return {"status": "ok"}

