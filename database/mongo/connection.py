from beanie import init_beanie, PydanticObjectId
from motor.motor_asyncio import AsyncIOMotorClient
from beanie import Document
from typing import Optional, List, Any
from pydantic_settings import BaseSettings
from pydantic import BaseModel

from models.mongo.events import Event
from models.mongo.users import User


class Settings(BaseSettings):
    DATABASE_URL: Optional[str] = None
    SECRET_KEY: Optional[str] = None

    async def initialize_database(self):
        client = AsyncIOMotorClient(self.DATABASE_URL)
        await init_beanie(database=client.get_database(), document_models=[Event, User])

    class Config:
        env_file = ".env"


class Database:
    def __init__(self, model: Document):
        self.model = model

    async def save(self, document: Document) -> None:
        await document.create()

    async def get_all(self) -> List[Any]:
        docs = await self.model.find_all().to_list()
        return docs

    async def get(self, id: PydanticObjectId) -> Any:
        doc = await self.model.get(id)
        if doc:
            return doc
        return False

    async def update(self, id: PydanticObjectId, body: BaseModel):
        desc_body = body.dict()
        desc_body = {k: v for k, v in desc_body.items() if v is not None}
        updated_query = {
            "$set": {field: value for field, value in desc_body.items()}
        }

        doc = await self.get(id)
        if not doc:
            return False

        await doc.update(updated_query)
        return doc

    async def delete(self, id: PydanticObjectId) -> bool:
        doc = await self.get(id)
        if not doc:
            return False

        await doc.delete()
        return True
