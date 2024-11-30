from fastapi import FastAPI, HTTPException
from model import Model
from prometheus_metrics import REQUEST_TIME
from fastapi.responses import Response
from datetime import datetime
from dotenv import load_dotenv
from pydantic import BaseModel
import os
import time
from model import Model
from prometheus_client import generate_latest, REGISTRY


app = FastAPI()

load_dotenv()

DB_CONFIG = {
    "host": os.getenv("DB_HOST"),
    "port": os.getenv("DB_PORT"),
    "dbname": os.getenv("DB_NAME"),
    "user": os.getenv("DB_USER"),
    "password": os.getenv("DB_PASSWORD"),
}
MLFLOW_TRACKING_URI = os.getenv("MLFLOW_TRACKING_URI")
MODEL_URI = os.getenv("MODEL_URI")
TICKET = os.getenv("TICKET")

class QueryModel(BaseModel):
    date: str


@app.post("/predict")
async def predict(date: QueryModel):
    try:
        input_date = datetime.strptime(date.date, "%Y-%m-%d").date()
    except ValueError:
        raise HTTPException(status_code=400, detail="Formato de data invalido. Use YYYY-MM-DD.")
    
    try:
        
        model = Model(tracking_uri=MLFLOW_TRACKING_URI,model_uri=MODEL_URI,db_config=DB_CONFIG,ticker=TICKET)
        
        start_time = time.time()
        predicts = model.predict(date=input_date)
        inference_time = time.time() - start_time

        REQUEST_TIME.observe(inference_time)
        
        return {"result" : predicts}
    
    except Exception as e :
        raise HTTPException(status_code=400, detail=f"Erro : {e}")
    
@app.get("/metrics")
async def metrics():
    return Response(generate_latest(REGISTRY), media_type="text/plain")