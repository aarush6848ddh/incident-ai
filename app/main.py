import app
from fastapi import FastAPI
from app.routers import health
from app.routers import incidents
from app.routers import ask
from app.routers import documents
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="Incident AI")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(health.router)
app.include_router(incidents.router)
app.include_router(ask.router)
app.include_router(documents.router)

