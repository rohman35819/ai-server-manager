# app/services/chat.py
import os
from fastapi import HTTPException
from openai import OpenAI
from app.models.chat import ChatRequest, ChatResponse

def _get_openai_client():
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        return None
    return OpenAI(api_key=api_key)

def get_chat_response(request: ChatRequest) -> ChatResponse:
    client = _get_openai_client()
    if client is None:
        # kembalikan error yang rapi ke user (500) agar tidak crash saat import
        raise HTTPException(status_code=500, detail="OPENAI_API_KEY not set in environment")

    # Panggil API baru (chat completions)
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": request.message}],
        max_tokens=150
    )

    # Ambil teks balasan — struktur response sesuai SDK v1.x
    reply_text = ""
    if response.choices and len(response.choices) > 0:
        # pesan ada di response.choices[0].message.content
        reply_text = response.choices[0].message.get("content") if isinstance(response.choices[0].message, dict) else getattr(response.choices[0].message, "content", "")
    return ChatResponse(reply=(reply_text or "").strip())
