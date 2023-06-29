from fastapi import FastAPI, Request
import redis
import json
import request
import asyncio

app = FastAPI()
redis_client = redis.Redis()

@app.post("/backendservice", status_code=201)
async def handle_backend(request: Request):
    event = await request.json()
    print(event)
    print("Received")
    # Forward the event
    return {"message": "Event forwarded successfully"}
