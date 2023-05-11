from fastapi import FastAPI
from config.db_config import connect_db


app = FastAPI()

if connect_db():
    print("Conexión exitosa con MongoDB")
else:
    print("Error al conectar con MongoDB")


@app.get("/")
async def root():
    return {"message": "Hello World"}

