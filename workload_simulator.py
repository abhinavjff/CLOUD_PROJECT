import requests
import random
import time

BASE_URL = "http://localhost:8000"

users = [101, 202, 303, 404, 505]
items = ["laptop", "book", "pen", "phone", "keyboard"]
queries = ["fastapi", "kafka", "python", "postgresql"]
files = ["report.pdf", "image.png", "notes.txt"]
amounts = [10.5, 20.0, 99.99, 5.25]

endpoints = [
    lambda: f"/request/{random.choice(users)}",
    lambda: f"/login/{random.choice(users)}",
    lambda: f"/logout/{random.choice(users)}",
    lambda: f"/purchase/{random.choice(users)}/{random.choice(items)}",
    lambda: f"/search/{random.choice(queries)}",
    lambda: f"/upload/{random.choice(users)}/{random.choice(files)}",
    lambda: f"/download/{random.choice(users)}/{random.choice(files)}",
    lambda: f"/profile/update/{random.choice(users)}",
    lambda: f"/payment/{random.choice(users)}/{random.choice(amounts)}",
    lambda: f"/notification/{random.choice(users)}",
    lambda: f"/delete/account/{random.choice(users)}",
    # NEW ERROR ENDPOINTS
    lambda: "/error",
    lambda: "/error/db",
    lambda: "/error/auth",
]


def simulate_traffic(num_requests=100, sleep_seconds=1):
    print(f"🚀 Simulating {num_requests} requests to FastAPI server...")
    for i in range(num_requests):
        endpoint = random.choice(endpoints)()
        url = BASE_URL + endpoint
        try:
            res = requests.get(url)
            print(f"[{i+1}] ✅ {url} -> {res.status_code} | {res.json()}")
        except Exception as e:
            print(f"[{i+1}] ❌ Failed to request {url}: {e}")
        time.sleep(sleep_seconds)

if __name__ == "__main__":
    simulate_traffic()
