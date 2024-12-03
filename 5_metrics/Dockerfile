FROM python:3.11-slim

WORKDIR /app

ENV DB_HOST=3_db
ENV DB_PORT=5432
ENV DB_NAME=db
ENV DB_USER=user
ENV DB_PASSWORD=password
ENV PROMETHEUS_URL=http://4_prometheus:9090

COPY database.py .
COPY main.py .
COPY metrics.py .
COPY requirements.txt .


RUN pip install --no-cache-dir --timeout 0 -r requirements.txt


EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]