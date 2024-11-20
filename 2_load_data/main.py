from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from datetime import datetime, timedelta, date
import yfinance as yf
from dotenv import load_dotenv
import hashlib
import os
from database import Db

app = FastAPI()

load_dotenv()

DB_CONFIG = {
    "host": os.getenv("DB_HOST"),
    "port": os.getenv("DB_PORT"),
    "dbname": os.getenv("DB_NAME"),
    "user": os.getenv("DB_USER"),
    "password": os.getenv("DB_PASSWORD"),
}

class QueryModel(BaseModel):
    ticker: str
    start_date: date
    end_date: date
    
def generate_hash(date_str):
    code_day = date_str.isoformat()
    return hashlib.md5(code_day.encode()).hexdigest()

@app.post("/load")
async def load(query: QueryModel):
    
    if query.start_date >= query.end_date:
        raise HTTPException(
            status_code=400,
            detail="A data inicial deve ser menor que a data final."
        )

    query.end_date = query.end_date + timedelta(days=1)

    ticker = query.ticker.strip()
    
    try:
        ticker = yf.Ticker(ticker)
        history = ticker.history(start=query.start_date.strftime("%Y-%m-%d"),
                                 end=query.end_date.strftime("%Y-%m-%d"))
        
        if history.empty:
            raise HTTPException(
                status_code=404,
                detail="Nenhum dado encontrado para o ticker com as datas informadas."
            )
        
        results = history.reset_index().to_dict(orient="records")
        
        results = [{**item, 'hash' : generate_hash(item['Date']), 'ticker' : query.ticker.strip()} for item in results]
        
        conn = Db(db_config = DB_CONFIG)
        
        conn.resgister_tickers_data(results)
        
        return { "msg": f"{len(results)} registro salvos com sucesso" }
    
    
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Erro ao buscar dados no YFinance: {e}"
        )
