from fastapi import FastAPI
from app.routers import health
from app.routers import incidents
from app.routers import ask
from app.routers import documents

app = FastAPI(title="Incident AI")

app.include_router(health.router)
app.include_router(incidents.router)
app.include_router(ask.router)
app.include_router(documents.router)

