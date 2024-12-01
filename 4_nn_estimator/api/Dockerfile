FROM python:3.11-slim

WORKDIR /app

ENV DB_HOST=3_db
ENV DB_PORT=5432
ENV DB_NAME=db
ENV DB_USER=user
ENV DB_PASSWORD=password
ENV MODEL_PATH=./model.pth
ENV TICKER=MSFT

COPY main.py .
COPY database.py .
COPY lstm.py .
COPY model.py .
COPY model.pth .
COPY prometheus_metrics.py .
COPY prometheus.yml .
COPY requirements.txt .

COPY mlruns ./mlruns


RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]