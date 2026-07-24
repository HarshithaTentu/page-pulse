import asyncio
import httpx
import re
import time

from app.cache import get_cached, set_cache


MAX_CONCURRENT_AUDITS = 20

semaphore = asyncio.Semaphore(MAX_CONCURRENT_AUDITS)


async def audit_url(url: str):

    # Check cache first
    cached_result = get_cached(url)

    if cached_result:
        cached_result["cached"] = True
        return cached_result

    start = time.perf_counter()

    try:
        async with semaphore:

            async with httpx.AsyncClient(timeout=10) as client:
                response = await client.get(url)

        elapsed = round(
            (time.perf_counter() - start) * 1000,
            2
        )

        title = ""

        match = re.search(
            r"<title>(.*?)</title>",
            response.text,
            re.IGNORECASE | re.DOTALL,
        )

        if match:
            title = match.group(1).strip()

        result = {
            "url": url,
            "status": response.status_code,
            "response_time_ms": elapsed,
            "title": title,
            "https": url.startswith("https"),
            "cached": False,
        }

        # Save result into cache
        set_cache(url, result)

        return result

    except httpx.TimeoutException:

        return {
            "url": url,
            "error": "Request timed out",
            "type": "TIMEOUT_ERROR",
        }

    except httpx.RequestError as e:

        return {
            "url": url,
            "error": str(e),
            "type": "REQUEST_ERROR",
        }

    except Exception as e:

        return {
            "url": url,
            "error": str(e),
            "type": "UNKNOWN_ERROR",
        }
