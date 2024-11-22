from database import Db
import os
from datetime import datetime
from dotenv import load_dotenv
import pandas as pd

load_dotenv()

os.getenv("FROM_DATE")

#UMA DATA QUE PODE SER USADA PARA SELECIONAR DADOS A PARTIR DE UMA DATA, QUANDO None PEGA TODOS OS DADOS
FROM_DATE =  os.getenv("FROM_DATE") if os.getenv("FROM_DATE") != 'None' else None 

DB_CONFIG = {
    "host": os.getenv("DB_HOST"),
    "port": os.getenv("DB_PORT"),
    "dbname": os.getenv("DB_NAME"),
    "user": os.getenv("DB_USER"),
    "password": os.getenv("DB_PASSWORD"),
}

if __name__ == '__main__':
    
    conn = Db(db_config = DB_CONFIG)#datetime.now().replace(hour=0, minute=1, second=0, microsecond=0).strftime("%Y-%m-%d")    
    tickers_data = conn.get_data_tickers(FROM_DATE)
    
    df = pd.DataFrame(data=tickers_data)
    
    print(df.head())
    
    
    