
FROM python:3.11-slim

WORKDIR /app

ENV DB_HOST=3_db
ENV DB_PORT=5432
ENV DB_NAME=db
ENV DB_USER=user
ENV DB_PASSWORD=password
ENV FROM_DATE=None
ENV TICKER=MSFT

COPY requirements.txt .
COPY database.py .
COPY generate_model.py .
COPY generate_model_pth.py .

COPY mlruns ./mlruns

RUN pip install --no-cache-dir --timeout 0 -r requirements.txt

EXPOSE 5000

CMD ["mlflow", "ui", "--host", "0.0.0.0", "--port", "5000"]