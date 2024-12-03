from fastapi import APIRouter, HTTPException
from app.shemas import MessageCreate, MessageResponse
from app.database import collection, redis_client
import json


router = APIRouter()


@router.get("/api/v1/messages", response_model=list[MessageResponse])
async def get_message():
    cached_data = await redis_client.get('messages_cache')
    if cached_data:
        return json.loads(cached_data)
    messages = await collection.find().to_list(100)
    result = [
        {
            "author": msg["author"],
            "content": msg["content"],
        }
        for msg in messages
    ]
    await redis_client.set('messages_cache', json.dumps(result))
    return result


@router.post("/api/v1/message", response_model=MessageResponse)
async def create_message(message: MessageCreate):
    new_message = message.dict()
    result = await collection.insert_one(new_message)
    if result.inserted_id:
        await redis_client.delete("messages_cache")
        return {**new_message, "id": str(result.inserted_id)}
    raise HTTPException(status_code=500, detail="Message not created")
