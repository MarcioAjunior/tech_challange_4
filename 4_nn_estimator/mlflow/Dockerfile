
FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
COPY main.py .
COPY lstm.py .
COPY tester.py .
COPY database.py .

COPY mlruns ./mlruns

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5000

CMD ["mlflow", "ui", "--host", "0.0.0.0", "--port", "5000"]