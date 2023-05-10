FROM python:3.9

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .
RUN /usr/local/bin/python -m pip install --upgrade pip

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
