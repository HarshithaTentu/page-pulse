from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.schemas import AuditRequest
from app.services import audit_url


app = FastAPI(
    title="Page Pulse API",
    description="Production-ready URL Audit Service",
    version="1.0.0",
)


# Allow frontend applications to access API
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def root():
    return {
        "message": "Page Pulse API is running"
    }


@app.post("/audit")
async def audit(request: AuditRequest):
    return await audit_url(str(request.url))
