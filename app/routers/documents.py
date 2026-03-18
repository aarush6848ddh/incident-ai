from fastapi import APIRouter, BackgroundTasks
from pydantic import BaseModel

router = APIRouter()

class IngestRequest(BaseModel):
    filename: str
    content: str

def process_document(filename: str, content: str):
    # This will eventually embed and index the document, but for now we just print it
    # For now, just simulate some processing time
    print(f"Processing document: {filename}")

@router.post("/documents/ingest")
def ingest_document(request: IngestRequest, background_tasks: BackgroundTasks):
    background_tasks.add_task(process_document, request.filename, request.content)
    return {"message": "Document received, processing in background."}