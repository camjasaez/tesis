from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
from motor.motor_asyncio import AsyncIOMotorClient
from config import settings
from contextlib import asynccontextmanager

# from api.routes.router import api_router
from api.routes import api_router


app = FastAPI()
app = FastAPI(title=settings["APP_NAME"], debug=settings["DEBUG_MODE"])
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings["ALLOWED_HOSTS"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(api_router, prefix="/api")


@asynccontextmanager
async def db_client():
    mongodb_client = AsyncIOMotorClient(settings["DB_URL"])
    mongodb = mongodb_client[settings["DB_NAME"]]
    print("DB connected")

    try:
        yield mongodb
    finally:
        mongodb_client.close()
        print("DB disconnected")


if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host=settings["HOST"],
        reload=settings["DEBUG_MODE"],
        port=settings["PORT"],
    )
