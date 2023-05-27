from pydantic import BaseSettings
from dotenv import load_dotenv

load_dotenv() 

class CommonSettings(BaseSettings):
    APP_NAME: str = "Detector-app"
    DEBUG_MODE: bool = False


class ServerSettings(BaseSettings):
    HOST: str = "0.0.0.0"
    PORT: int = 8000


class DatabaseSettings(BaseSettings):
    DB_URL: str
    DB_NAME: str


class Settings(CommonSettings, ServerSettings, DatabaseSettings):
    pass


settings = Settings()
