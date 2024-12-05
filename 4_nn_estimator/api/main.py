from fastapi import FastAPI, HTTPException
from model import Model
from prometheus_metrics import REQUEST_TIME
from fastapi.responses import Response
from datetime import datetime, timedelta
from dotenv import load_dotenv
from pydantic import BaseModel
import os
import time
from model import Model
from prometheus_client import generate_latest, REGISTRY
from database import Db
from prepare_result import prepare_date_to_api


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

TIMES_RETURNS = 7

class QueryModel(BaseModel):
    date: str


@app.post("/predict")
async def predict(date: QueryModel):
    
    try:
        input_date = datetime.strptime(date.date, "%Y-%m-%d").date()
    except ValueError:
        raise HTTPException(status_code=400, detail="Formato de data invalido. Use YYYY-MM-DD.")
    
    verify_date_range = datetime.now().date() + timedelta(days=6)
    
    if (input_date > verify_date_range):
        raise HTTPException(status_code=400, detail="Não é possível informar uma data superior a 7 dias de previsão")
    
    try:
        
        db = Db(db_config=DB_CONFIG)
        bigger_date_db = db.get_bigger_date()[0]
        
        difference_days = int((input_date - datetime.date(bigger_date_db)).days)

        limit_fetch = TIMES_RETURNS - difference_days

        db_latests_results = db.get_latests_results(limit = limit_fetch)
        
        model = Model(model_path=MODEL_PATH,db_config=DB_CONFIG,ticker=TICKER)
        
        start_time = time.time()
        predicts = model.predict(date=input_date)
        inference_time = time.time() - start_time

        REQUEST_TIME.observe(inference_time)
        
        results = prepare_date_to_api(db_latests_results,predicts)
        
        return {"result" : results}
    
    except Exception as e :
        raise HTTPException(status_code=400, detail=f"Erro : {e}")
    
@app.get("/metrics")
async def metrics():
    return Response(generate_latest(REGISTRY), media_type="text/plain")