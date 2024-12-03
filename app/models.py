from pydantic import BaseModel


class Message(BaseModel):
    author: str
    content: str
