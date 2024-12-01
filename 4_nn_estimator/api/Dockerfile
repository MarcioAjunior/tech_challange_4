FROM python:3.11-slim

WORKDIR /app


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