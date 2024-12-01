from fastapi import FastAPI, HTTPException
from dotenv import load_dotenv
from metrics import Metrics
import os

app = FastAPI()

load_dotenv()

DB_CONFIG = {
    "host": os.getenv("DB_HOST"),
    "port": os.getenv("DB_PORT"),
    "dbname": os.getenv("DB_NAME"),
    "user": os.getenv("DB_USER"),
    "password": os.getenv("DB_PASSWORD"),
}

PROMETHEUS_URL=os.getenv("PROMETHEUS_URL")

@app.get("/metrics")
async def metrics():
    
    mse = Metrics.mse(db_config = DB_CONFIG)
    
    data_drift = Metrics.data_drift(db_config = DB_CONFIG)
    
    avg_time_inference = Metrics.avg_time_inference(prometheus_url=PROMETHEUS_URL)
    
    return {"mse" : mse, "data_drift" : data_drift, "avg_time_inference" : avg_time_inference}