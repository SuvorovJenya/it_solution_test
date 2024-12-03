from pydantic import BaseModel


class MessageCreate(BaseModel):
    author: str
    content: str


class MessageResponse(BaseModel):
    author: str
    content: str
