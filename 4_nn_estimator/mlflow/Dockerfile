
FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
COPY database.py .
COPY generate_model.py .

COPY mlruns ./mlruns

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5000

CMD ["mlflow", "ui", "--host", "0.0.0.0", "--port", "5000"]