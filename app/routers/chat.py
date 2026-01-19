from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy import select
from sqlalchemy.orm import Session

from app.database import get_db
from app.models.conversation import Conversation
from app.models.message import Message
from app.models.user import User
from app.schemas.chat import ChatRequest, ChatResponse, MessageOut
from app.schemas.conversation import ConversationOut, ConversationWithMessages
from app.services.llm import generate_reply
from app.utils.jwt import get_current_user


router = APIRouter(tags=["chat"])


@router.post("/chat", response_model=ChatResponse)
def chat(
    payload: ChatRequest,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
) -> ChatResponse:
    conversation = None
    if payload.conversation_id:
        conversation = db.execute(
            select(Conversation).where(
                Conversation.id == payload.conversation_id, Conversation.user_id == current_user.id
            )
        ).scalar_one_or_none()
        if conversation is None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Conversation not found")
    else:
        conversation = Conversation(user_id=current_user.id)
        db.add(conversation)
        db.flush()

    previous_messages = db.execute(
        select(Message)
        .where(Message.conversation_id == conversation.id)
        .order_by(Message.created_at.asc())
    ).scalars()

    llm_messages = [
        {"role": message.role, "content": message.content} for message in previous_messages
    ]
    llm_messages.append({"role": "user", "content": payload.message})

    reply = generate_reply(llm_messages)

    user_message = Message(conversation_id=conversation.id, role="user", content=payload.message)
    assistant_message = Message(conversation_id=conversation.id, role="assistant", content=reply)
    db.add_all([user_message, assistant_message])
    db.commit()

    return ChatResponse(conversation_id=conversation.id, reply=reply)


@router.get("/conversations", response_model=list[ConversationOut])
def list_conversations(
    db: Session = Depends(get_db), current_user: User = Depends(get_current_user)
) -> list[ConversationOut]:
    conversations = db.execute(
        select(Conversation)
        .where(Conversation.user_id == current_user.id)
        .order_by(Conversation.created_at.desc())
    ).scalars()
    return [ConversationOut(id=conv.id, created_at=conv.created_at) for conv in conversations]


@router.get("/conversations/{conversation_id}", response_model=ConversationWithMessages)
def get_conversation(
    conversation_id: UUID,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
) -> ConversationWithMessages:
    conversation = db.execute(
        select(Conversation).where(
            Conversation.id == conversation_id, Conversation.user_id == current_user.id
        )
    ).scalar_one_or_none()
    if conversation is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Conversation not found")

    messages = db.execute(
        select(Message)
        .where(Message.conversation_id == conversation.id)
        .order_by(Message.created_at.asc())
    ).scalars()
    message_out = [
        MessageOut(id=msg.id, role=msg.role, content=msg.content, created_at=msg.created_at)
        for msg in messages
    ]
    return ConversationWithMessages(
        id=conversation.id, created_at=conversation.created_at, messages=message_out
    )

