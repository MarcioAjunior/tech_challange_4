import os
from datetime import datetime, timedelta
import requests
import psycopg2
from psycopg2.extras import RealDictCursor
from dotenv import load_dotenv
import schedule
import time
from concurrent.futures import ThreadPoolExecutor

load_dotenv()

DAYS_INTERVAL = int(os.getenv("DAYS_INTERVAL", 7))
API_URL = os.getenv("API_URL")
DB_CONFIG = {
    "host": os.getenv("DB_HOST"),
    "port": os.getenv("DB_PORT"),
    "dbname": os.getenv("DB_NAME"),
    "user": os.getenv("DB_USER"),
    "password": os.getenv("DB_PASSWORD"),
}
TICKER = os.getenv("TICKER")
NN_ESTIMATOR_NAME = os.getenv("NN_ESTIMATOR_NAME")
NN_API_URL = os.getenv("NN_API_URL")

def async_request(payload):
    
    print('Init thread')
    
    try:
        response = requests.post(NN_API_URL + '/fine_tunning', json=payload, timeout=5000)
        print(f"Send requisição: {response.status_code}")
    except requests.RequestException as e:
        print(f"Erro ao enviar requisição: {e}")

def load_data_to_api():
    end_date = datetime.now().replace(hour=0, minute=1, second=0, microsecond=0)
    start_date = end_date - timedelta(days=DAYS_INTERVAL)

    try:
        payload = {
            "ticker": TICKER,
            "start_date": start_date.strftime("%Y-%m-%d"),
            "end_date": end_date.strftime("%Y-%m-%d"),
        }
        
        response = requests.post(f"{API_URL}/load", json=payload)
        response.raise_for_status()
        print("Resposta da API:", response.json())
    except requests.RequestException as e:
        print(f"Erro na chamada da API: {e}")
        return

    query = "select max(date) from lb_tickers_data;" 

    try:
        with psycopg2.connect(**DB_CONFIG) as conn:
            with conn.cursor(cursor_factory=RealDictCursor) as cursor:
                cursor.execute(query)
                result = cursor.fetchone()
                max_date = result.get('max', datetime.now())
                max_date = max_date + timedelta(days=DAYS_INTERVAL)
                today_date = datetime.now().replace(hour=0, minute=1, second=0, microsecond=0)
                
                if max_date.replace(tzinfo=None) <= today_date.replace(tzinfo=None):
                    
                    executor = ThreadPoolExecutor(max_workers=1)
                    executor.submit(async_request,{"need_fine_tunning" : True})  
                
    except psycopg2.Error as e:
        print(f"Erro ao consultar o banco de dados: {e}")

schedule.every(DAYS_INTERVAL).minutes.do(load_data_to_api).at("00:10").do(load_data_to_api)
#schedule.every(1).seconds.do(load_data_to_api)

print("Iniciando o script Shepherd")
while True:
    schedule.run_pending()
    time.sleep(1)
