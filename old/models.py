from typing import List
from pydantic import BaseModel


class Todo(BaseModel):
    id: int
    item: str

    class Config:
        json_schema_extra = {
            'example': {
                'id': 1,
                "item": "Example schema!"
            }
        }


class TodoItem(BaseModel):
    item: str

    class Config:
        json_schema_extra = {
            'example': {
                'item': 'Read the next chapter of the book'
            }
        }


class TodoItems(BaseModel):
    todos: List[Todo]

    class Config:
        json_schema_extra = {
            "example": {
                "todos": [
                    {
                        "id": 1,
                        "item": "Example schema 1!"
                    },
                    {
                        "id": 2,
                        "item": "Example schema 2!"
                    }
                ]
            }
        }
