from beanie import Document
from typing import Optional, List
from pydantic import BaseModel


class Event(Document):
    creator: Optional[str] = None
    title: str
    image: str
    description: str
    tags: List[str]
    location: str

    class Config:
        json_schema_extra = {
            "example": {
                "title": "FastAPI Book Launch",
                "image": "https://google.com",
                "description": "We will be discussing",
                "tags": ["python", "fastapi", "book"],
                "location": "Google Meet"
            }
        }


class EventUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    image: Optional[str] = None
    tags: Optional[List[str]] = None
    location: Optional[str] = None

    class Config:
        json_schema_extra = {
            "example": {
                "title": "FastAPI Book Launch put",
                "description": "We will be discussing put",
            }
        }
