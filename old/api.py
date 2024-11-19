from fastapi import FastAPI
from todo import todo_router
import uvicorn

app = FastAPI()
app.include_router(todo_router)


@app.get("/")
async def welcome() -> dict:
    return {
        "message": "Hello World"
    }


if __name__ == "__main__":
    uvicorn.run("api:app", host="0.0.0.0", port=8000, reload=True)
