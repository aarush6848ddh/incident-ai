from fastapi import FastAPI
from app.routers import health

app = FastAPI(title="Incident AI")

app.include_router(health.router)

