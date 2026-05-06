from fastapi import FastAPI
from src.api.auth import router as auth_router
from src.api.quest import router as quest_router

import uvicorn


app = FastAPI()
app.include_router(auth_router)
app.include_router(quest_router)


if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)