from openai import OpenAI
from app.models.chat import ChatRequest, ChatResponse

client = OpenAI()

def get_chat_response(request: ChatRequest) -> ChatResponse:
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",  # bisa ganti ke "gpt-4" kalau ada akses
        messages=[
            {"role": "user", "content": request.message}
        ],
        max_tokens=150
    )
    return ChatResponse(reply=response.choices[0].message.content.strip())
