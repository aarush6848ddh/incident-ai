from fastapi import APIRouter, Depends
from pydantic import BaseModel
from enum import Enum
from app.auth import verify_api_key
import app.database
import app.models
from sqlalchemy.orm import Session

router = APIRouter()


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
def create_incident(incident: IncidentCreate, db: Session = Depends(app.database.get_db)):
    new_incident = app.models.Incident(
        title=incident.title,
        severity=incident.severity,
        description=incident.description
    )
    db.add(new_incident)
    db.commit()
    db.refresh(new_incident)
    return new_incident

@router.get("/incidents", dependencies=[Depends(verify_api_key)])
def get_incidents(db: Session = Depends(app.database.get_db)):
    return db.query(app.models.Incident).all()
