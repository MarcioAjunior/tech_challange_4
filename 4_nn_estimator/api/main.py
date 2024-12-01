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
MODEL_PATH = os.getenv("MODEL_PATH")
TICKER = os.getenv("TICKER")

class QueryModel(BaseModel):
    date: str


@app.post("/predict")
async def predict(date: QueryModel):
    try:
        input_date = datetime.strptime(date.date, "%Y-%m-%d").date()
    except ValueError:
        raise HTTPException(status_code=400, detail="Formato de data invalido. Use YYYY-MM-DD.")
    
    try:
        
        model = Model(model_path=MODEL_PATH,db_config=DB_CONFIG,ticker=TICKER)
        
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