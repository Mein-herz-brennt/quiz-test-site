from fastapi import FastAPI
from src.api.auth import router as auth_router
from src.database import create_db
import uvicorn

create_db()
app = FastAPI()
app.include_router(auth_router)


if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)