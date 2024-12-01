FROM python:3.11-slim

WORKDIR /app

COPY database.py .
COPY lstm.py .
COPY main.py .
COPY model.py .
COPY model.pth .
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]