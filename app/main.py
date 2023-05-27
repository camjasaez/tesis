from fastapi import FastAPI
from config.db_config import connect_db


app = FastAPI()

# Conexión a la base de datos
connect_db()


@app.get("/")
async def root():
    print("Hello World")
    return {"message": "Hello World"}

