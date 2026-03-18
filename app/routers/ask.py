from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()

class AskRequest(BaseModel):
    question: str

@router.post("/ask")
def ask_question(request: AskRequest):
    response = {"answer": "This feature is not implemented yet."}
    return response

