import time
import uuid
import logging

from fastapi import Request
from fastapi.responses import JSONResponse

from app.rate_limit import is_rate_limited


logging.basicConfig(
    level=logging.INFO,
    format="%(message)s"
)


logger = logging.getLogger("page-pulse")


async def request_logger(request: Request, call_next):

    request_id = str(uuid.uuid4())

    client_ip = request.client.host

    # Rate limit check
    if is_rate_limited(client_ip):

        logger.warning(
            {
                "request_id": request_id,
                "client_ip": client_ip,
                "error": "RATE_LIMIT_EXCEEDED",
            }
        )

        return JSONResponse(
            status_code=429,
            content={
                "error": "Too many requests",
                "type": "RATE_LIMIT_EXCEEDED",
                "request_id": request_id,
            },
        )

    start = time.perf_counter()

    response = await call_next(request)

    elapsed = round(
        (time.perf_counter() - start) * 1000,
        2
    )

    logger.info(
        {
            "request_id": request_id,
            "method": request.method,
            "path": request.url.path,
            "client_ip": client_ip,
            "status": response.status_code,
            "response_time_ms": elapsed,
        }
    )

    response.headers["X-Request-ID"] = request_id

    return response
