from fastapi import APIRouter
from models.chat_models import ChatRequest
from services.ai_service import generate_ai_response

router = APIRouter()

@router.post("/chat")
def chat_endpoint(payload: ChatRequest):
    response = generate_ai_response(payload.message)
    return {"response": response}
