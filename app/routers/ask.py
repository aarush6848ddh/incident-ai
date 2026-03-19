from fastapi import APIRouter, Depends
from pydantic import BaseModel
from app.auth import verify_api_key


router = APIRouter()

class AskRequest(BaseModel):
    question: str

@router.post("/ask", dependencies=[Depends(verify_api_key)])
def ask_question(request: AskRequest):
    response = {"answer": "This feature is not implemented yet."}
    return response

