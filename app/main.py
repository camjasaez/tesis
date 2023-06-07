from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
from config import settings
from api.routes import api_router


app = FastAPI(title=settings["APP_NAME"], debug=settings["DEBUG_MODE"])
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings["ALLOWED_HOSTS"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(api_router, prefix="/api")


if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host=settings["HOST"],
        reload=settings["DEBUG_MODE"],
        port=settings["PORT"],
    )
