from fastapi import APIRouter, Depends
from pydantic import BaseModel
from enum import Enum
from app.auth import verify_api_key


router = APIRouter()

incidents_db = []

class Severity(str, Enum):
    low = "low"
    medium = "medium"
    high = "high"
    critical = "critical"

class IncidentCreate(BaseModel):
    title: str
    severity: Severity
    description: str

@router.post("/incidents", dependencies=[Depends(verify_api_key)])
def create_incident(incident: IncidentCreate):
    new_incident = {
        "id": len(incidents_db) + 1,
        "title": incident.title,
        "severity": incident.severity,
        "description": incident.description,
        "status": "open"
    }
    incidents_db.append(new_incident)
    return new_incident

@router.get("/incidents", dependencies=[Depends(verify_api_key)])
def get_incidents():
    return incidents_db
