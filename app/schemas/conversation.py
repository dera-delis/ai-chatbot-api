from datetime import datetime
from uuid import UUID

from pydantic import BaseModel

from app.schemas.chat import MessageOut


class ConversationOut(BaseModel):
    id: UUID
    created_at: datetime


class ConversationWithMessages(BaseModel):
    id: UUID
    created_at: datetime
    messages: list[MessageOut]

