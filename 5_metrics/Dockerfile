FROM python:3.11-slim

WORKDIR /app

COPY database.py .
COPY main.py .
COPY metrics.py .
COPY requirements.txt .


RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8000