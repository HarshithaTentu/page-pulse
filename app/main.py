from fastapi import FastAPI

from app.schemas import AuditRequest
from app.services import audit_url
from app.middleware import request_logger


app = FastAPI(
    title="Page Pulse API",
    description="Production-ready URL Audit Service",
    version="1.0.0",
)


# Add request logging middleware
app.middleware("http")(request_logger)


@app.get("/")
async def root():
    return {
        "message": "Page Pulse API is running 🚀"
    }


@app.post("/audit")
async def audit(request: AuditRequest):
    return await audit_url(str(request.url))
