from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.schemas import AuditRequest
from app.services import audit_url


app = FastAPI(
    title="Page Pulse API",
    description="Production-ready URL Audit Service",
    version="1.0.0",
)


app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "https://page-pulse-vj8z.vercel.app",
        "http://localhost:5500"
    ],
    allow_credentials=True,
    allow_methods=["GET", "POST", "OPTIONS"],
    allow_headers=["*"],
)


@app.get("/")
async def root():
    return {
        "message": "Page Pulse API is running"
    }


@app.options("/audit")
async def audit_options():
    return {}


@app.post("/audit")
async def audit(request: AuditRequest):
    return await audit_url(str(request.url))
