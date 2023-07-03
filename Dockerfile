# Dockerfile para la api de la aplicación
# Usa una imagen base de Python
FROM python:3.9

# Establece el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copia los archivos de la aplicación al contenedor
COPY /app /app

# Instala las dependencias
RUN pip install --no-cache-dir --upgrade -r requirements.txt

# Expone el puerto en el que se ejecuta la aplicación
EXPOSE 8000

# Ejecuta el comando para iniciar la aplicación
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
