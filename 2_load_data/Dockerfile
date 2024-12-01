FROM python:3.11-slim

WORKDIR /app

ENV DB_HOST=3_db
ENV DB_PORT=5432
ENV DB_NAME=db
ENV DB_USER=user
ENV DB_PASSWORD=password
ENV MODEL_PATH=./model.pth

COPY database.py .
COPY lstm.py .
COPY main.py .
COPY model.py .
COPY model.pth .
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]