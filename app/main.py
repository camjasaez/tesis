from fastapi import FastAPI
# from config.db_config import connect_db


app = FastAPI()

# if connect_db():
#     print(" => Conexión exitosa con MongoDB")
# else:
#     print(" =X Error al conectar con MongoDB")


@app.get("/")
async def root():
    print("Hello World")
    return {"message": "Hello World"}

