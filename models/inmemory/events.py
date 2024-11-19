from typing import List
from pydantic import BaseModel


class Event(BaseModel):
    id: int
    title: str
    image: str
    description: str
    tags: List[str]
    location: str

    class Config:
        json_schema_extra = {
            "example": {
                "id": 1,
                "title": "FastAPI Book Launch",
                "image": "https://google.com",
                "description": "We will be discussing",
                "tags": ["python", "fastapi", "book"],
                "location": "Google Meet"
            }
        }
