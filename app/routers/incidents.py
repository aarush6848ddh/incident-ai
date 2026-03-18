from fastapi import APIRouter
from pydantic import BaseModel
from enum import Enum

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

@router.post("/incidents")
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

@router.get("/incidents")
def get_incidents():
    return incidents_db
