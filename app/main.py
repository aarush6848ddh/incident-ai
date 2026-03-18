from fastapi import FastAPI
from app.routers import health
from app.routers import incidents

app = FastAPI(title="Incident AI")

app.include_router(health.router)
app.include_router(incidents.router)

