import os
from datetime import datetime, timedelta
import requests
import psycopg2
from psycopg2.extras import RealDictCursor
from dotenv import load_dotenv
import schedule
import time

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

def load_data_to_api():
    end_date = datetime.now().replace(hour=0, minute=1, second=0, microsecond=0)
    start_date = end_date - timedelta(days=DAYS_INTERVAL)

    print(f"Enviando payload para API: {payload}")
    try:
        payload = {
            "start_date": start_date.isoformat(),
            "end_date": end_date.isoformat(),
        }
        response = requests.post(f"{API_URL}/load", json=payload)
        response.raise_for_status()
        print("Resposta da API:", response.json())
    except requests.RequestException as e:
        print(f"Erro na chamada da API: {e}")
        return

    query = """
        select * from lb_nn_estimator;
    """

    try:
        with psycopg2.connect(**DB_CONFIG) as conn:
            with conn.cursor(cursor_factory=RealDictCursor) as cursor:
                cursor.execute(query)
                results = cursor.fetchall()
                print("Resultados da consulta ao banco de dados:")
                for row in results:
                    print(row)
    except psycopg2.Error as e:
        print(f"Erro ao consultar o banco de dados: {e}")

schedule.every(DAYS_INTERVAL).minutes.do(load_data_to_api).at("00:01").do(load_data_to_api)
#schedule.every(1).minutes.do(load_data_to_api)

print("Iniciando o script Shepherd")
while True:
    schedule.run_pending()
    time.sleep(1)
