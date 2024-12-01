from sklearn.metrics import mean_squared_error
from scipy.stats import ks_2samp
from database import Db
import numpy as np
import pandas as pd
import requests

class Metrics:
    
    @staticmethod
    def mse(db_config = {}):
        conn = Db(db_config = db_config)
        results = conn.get_data_to_mse()
        df = pd.DataFrame(results)
        mse = mean_squared_error(df['close'], df['predicted'])
        return str(mse)
    
    @staticmethod
    def data_drift(db_config = {}):
        
        conn = Db(db_config = db_config)
        reference, current = conn.get_data_to_data_drift()
        
        df_reference, df_current = pd.DataFrame(reference), pd.DataFrame(current)
        
        stat, p_value = ks_2samp(df_reference['close'], df_current['predicted'])
        
        return {
            "ks_statistic": str(stat),
            "p_value": "{:.20f}".format(p_value) ,
            "drift_detected": float(p_value) < 0.007  # (nível de significância)
        }    
    
    
    @staticmethod
    def avg_time_inference(prometheus_url = ''):
        try:
            prometheus_url = f'{prometheus_url}/api/v1/query'
            query = "model_inference_time_seconds_sum / model_inference_time_seconds_count"
            params = {
                "query": query
            }
            response = requests.get(prometheus_url, params=params)
            
            if response.status_code == 200:
                try:
                    metrics_data = response.json()
                    
                    if "data" in metrics_data and "result" in metrics_data["data"]:
                        result = metrics_data["data"]["result"]
                        if result:
                            avg_inference_time = result[0]["value"][1]
                            return avg_inference_time
                        else:
                            print("Nenhum dado encontrado para a consulta.")
                    else:
                        print("Erro na resposta da consulta")
                except ValueError as e:
                    print(f"Erro ao processar JSON: {e}")
        
        except Exception as e:
            raise RuntimeError(f"Erro ao calcular o tempo médio: {e}")