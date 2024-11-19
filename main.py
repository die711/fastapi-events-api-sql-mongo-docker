from fastapi import FastAPI

import uvicorn

# from routes.inmemory.events import event_router
# from routes.inmemory.users import user_router

# from routes.sql.events import event_router
# from database.sql.connection import conn

from routes.mongo.events import event_router
from routes.mongo.users import user_router

from database.mongo.connection import Settings

app = FastAPI()
settings = Settings()

app.include_router(event_router, prefix="/event")
app.include_router(user_router, prefix="/user")


# app.include_router(user_router, prefix="/user")

@app.on_event("startup")
async def on_startup():
    # conn()
    await settings.initialize_database()


@app.get("/")
async def home():
    return {
        "hello": "world"
    }


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
