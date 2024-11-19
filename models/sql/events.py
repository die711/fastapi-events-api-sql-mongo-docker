from sqlmodel import JSON, SQLModel, Field, Column
from typing import Optional, List


class Event(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    title: str
    image: str
    description: str
    tags: List[str] = Field(sa_column=Column(JSON))
    location: str

    class Config:
        arbitrary_types_allowed = True

        json_schema_extra = {
            "example": {
                "title": "FastAPI Book Launch",
                "image": "https://google.com",
                "description": "We will be discussing",
                "tags": ["python", "fastapi", "book"],
                "location": "Google Meet"
            }
        }


class EventUpdate(SQLModel):
    title: Optional[str] = None
    image: Optional[str] = None
    description: Optional[str] = None
    tags: Optional[List[str]] = None
    location: Optional[str] = None

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
