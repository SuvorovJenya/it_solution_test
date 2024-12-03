from motor.motor_asyncio import AsyncIOMotorClient
from redis import asyncio as aioredis

mongo_client = AsyncIOMotorClient("mongodb://mongo:27017")
db = mongo_client["messages_db"]
collection = db["messages"]

redis_client = aioredis.from_url("redis://redis:6379", decode_responses=True)
