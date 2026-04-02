from fastapi import APIRouter
from schemas.chat import ChatRequest, ChatResponse
from services.llm_service import chat_with_vllm

router = APIRouter(tags=["Chat"])

@router.post("/chat", response_model= ChatResponse)
def chat(req: ChatRequest):
    result = chat_with_vllm(req.messages)
    return ChatResponse(response=result)
