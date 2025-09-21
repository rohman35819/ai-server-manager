from fastapi import APIRouter
from app.models.chat import ChatRequest, ChatResponse
from app.services.chat import get_chat_response

router = APIRouter()

@router.post("/", response_model=ChatResponse)
async def chat(request: ChatRequest):
    return get_chat_response(request)
