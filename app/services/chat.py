import openai
from app.models.chat import ChatRequest, ChatResponse

openai.api_key = "YOUR_OPENAI_API_KEY"

def get_chat_response(request: ChatRequest) -> ChatResponse:
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=request.message,
        max_tokens=150
    )
    return ChatResponse(reply=response.choices[0].text.strip())
