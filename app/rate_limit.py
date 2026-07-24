import time
import os


RATE_LIMIT = int(os.getenv("RATE_LIMIT", "10"))
RATE_WINDOW = int(os.getenv("RATE_WINDOW", "60"))


clients = {}


def is_rate_limited(client_ip: str):

    current_time = time.time()

    if client_ip not in clients:
        clients[client_ip] = []

    # Remove expired requests
    clients[client_ip] = [
        timestamp
        for timestamp in clients[client_ip]
        if current_time - timestamp < RATE_WINDOW
    ]

    # Check limit
    if len(clients[client_ip]) >= RATE_LIMIT:
        return True

    # Store request
    clients[client_ip].append(current_time)

    return False
