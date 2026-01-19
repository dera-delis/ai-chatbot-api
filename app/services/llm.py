import logging

from openai import OpenAI
from openai.types.chat import ChatCompletionMessageParam

from app.config import settings


logger = logging.getLogger(__name__)


def generate_reply(messages: list[ChatCompletionMessageParam]) -> str:
    if not settings.openai_api_key:
        return "AI service unavailable"

    client = OpenAI(api_key=settings.openai_api_key)
    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=messages,
            temperature=0.3,
            timeout=20,
        )
        return response.choices[0].message.content or ""
    except Exception:
        logger.exception("LLM request failed")
        return "AI service unavailable"

