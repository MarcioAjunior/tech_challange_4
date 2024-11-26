from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from datetime import datetime, timedelta, date
import yfinance as yf
from dotenv import load_dotenv
import hashlib
import os
from database import Db
from model import Model

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

class QueryModel(BaseModel):
    ticker: str
    start_date: date
    end_date: date
    
def generate_hash(date_str):
    return hashlib.md5(date_str.encode()).hexdigest()

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
        
        #history = yf.download(ticker, start=query.start_date.strftime("%Y-%m-%d"), end=query.end_date.strftime("%Y-%m-%d"))
        history = yf.download(ticker)
        history.reset_index(inplace=True)

        if history.empty:
            raise HTTPException(
                status_code=404,
                detail="Nenhum dado encontrado para o ticker com as datas informadas."
            )

        model = Model(tracking_uri=MLFLOW_TRACKING_URI,model_uri=MODEL_URI,db_config=DB_CONFIG,ticker=ticker)
        
        results = []
                    
        for _, row in history.iterrows():
                        
            predicted = model.predict(date=row['Date'].item().to_pydatetime().strftime('%Y-%m-%d'))
            print(predicted, 'predicted')
            raise Exception('AAA')
                        
            new_row = {
                'hash': str(row['Date'].item().to_pydatetime()),
                'ticker': ticker,
                'date': row['Date'].item().to_pydatetime(),
                'open': row['Open'].item(),
                'high': row['High'].item(),
                'low': row['Low'].item(),
                'close': row['Close'].item(),
                'price': None,
                'volume': row['Volume'].item(),
                'predicted' : predicted
            }

            results.append(new_row)
        
        conn = Db(db_config = DB_CONFIG)
        
        conn.resgister_tickers_data(results)
        
        return { "msg": f"{len(results)} registro salvos com sucesso" }

        
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Erro ao buscar dados no YFinance: {e}"
        )

