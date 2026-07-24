import time
import os

CACHE_TTL = int(os.getenv("CACHE_TTL", "300"))

cache = {}


def get_cached(url: str):
    if url not in cache:
        return None

    timestamp, data = cache[url]

    if time.time() - timestamp > CACHE_TTL:
        del cache[url]
        return None

    return data


def set_cache(url: str, data):
    cache[url] = (time.time(), data)
