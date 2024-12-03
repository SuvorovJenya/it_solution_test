from fastapi import FastAPI
from app.routers import messages

app = FastAPI()

app.include_router(messages.router)
