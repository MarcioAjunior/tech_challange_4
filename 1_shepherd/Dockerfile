FROM python:3.11-slim

ENV DAYS_INTERVAL=1
ENV API_URL=http://2_load_data:8000
ENV NN_API_URL=http://4_nn_estimator:8000
ENV NN_ESTIMATOR_NAME=estimator1
ENV DB_HOST=3_db
ENV DB_PORT=5432
ENV DB_NAME=db
ENV DB_USER=user
ENV DB_PASSWORD=password
ENV TICKER=MSFT

WORKDIR /app

COPY requirements.txt .
COPY main.py .

RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "main.py"]
