from fastapi import FastAPI, Request
from kafka import KafkaProducer
import json
import time

app = FastAPI()

# Kafka Producer Setup
producer = KafkaProducer(
    bootstrap_servers="localhost:9092",
    value_serializer=lambda v: json.dumps(v).encode("utf-8")
)

# Middleware for logging requests with enhanced observability
@app.middleware("http")
async def log_request_data(request: Request, call_next):
    start_time = time.time()
    response = await call_next(request)
    duration_ms = int((time.time() - start_time) * 1000)

    user_id = request.path_params.get("user_id", None)

    # Classify request as error or normal based on path or status
    event_type = "error" if "/error" in request.url.path or response.status_code >= 400 else "API request"

    log_data = {
        "user_id": user_id,
        "event": event_type,
        "endpoint": request.url.path,
        "response_time_ms": duration_ms,
        "status_code": response.status_code
    }

    producer.send("api-requests", log_data)
    return response

# --- API Endpoints ---

@app.get("/")
def home():
    return {"message": "API is running"}

@app.get("/request/{user_id}")
def handle_request(user_id: int):
    return {"message": f"Request received from user {user_id}"}

@app.get("/error/db")
def db_error(request: Request):
    log_data = {
        "user_id": None,
        "event": "Database Error",
        "endpoint": str(request.url.path),
        "response_time_ms": 0
    }
    producer.send("api-requests", log_data)
    return {"message": "Database connection failed"}

@app.get("/error/auth")
def auth_error(request: Request):
    log_data = {
        "user_id": None,
        "event": "Authentication Failed",
        "endpoint": str(request.url.path),
        "response_time_ms": 0
    }
    producer.send("api-requests", log_data)
    return {"message": "Invalid credentials"}



@app.get("/login/{user_id}")
def login(user_id: int):
    return {"message": f"User {user_id} logged in"}

@app.get("/logout/{user_id}")
def logout(user_id: int):
    return {"message": f"User {user_id} logged out"}

@app.get("/purchase/{user_id}/{item}")
def purchase(user_id: int, item: str):
    return {"message": f"User {user_id} purchased {item}"}

@app.get("/search/{query}")
def search(query: str):
    return {"message": f"Searched for {query}"}

@app.get("/upload/{user_id}/{file_name}")
def upload(user_id: int, file_name: str):
    return {"message": f"User {user_id} uploaded {file_name}"}

@app.get("/download/{user_id}/{file_name}")
def download(user_id: int, file_name: str):
    return {"message": f"User {user_id} downloaded {file_name}"}

@app.get("/profile/update/{user_id}")
def profile_update(user_id: int):
    return {"message": f"User {user_id} updated profile"}

@app.get("/payment/{user_id}/{amount}")
def payment(user_id: int, amount: float):
    return {"message": f"User {user_id} made a payment of ${amount}"}

@app.get("/notification/{user_id}")
def notification(user_id: int):
    return {"message": f"User {user_id} received a notification"}

@app.get("/delete/account/{user_id}")
def delete_account(user_id: int):
    return {"message": f"User {user_id} deleted account"}

# Run with: uvicorn api_server:app --reload
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
