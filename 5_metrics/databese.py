import psycopg2
from psycopg2.extras import execute_values

class Db:
    _instance = None
    _config = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls)
            cls._config = kwargs.get("db_config")
            cls._instance.init_connection(kwargs.get("db_config"))
            
        return cls._instance

    def init_connection(self, db_config):
        if not db_config:
            raise ValueError("configuração do banco incorreta")
        
        self.connection = psycopg2.connect(**db_config)
        self.connection.autocommit = True
        self.cursor = self.connection.cursor()
    
    def close_connection(self):
        if self.connection:
            self.cursor.close()
            self.connection.close()

    def get_data_to_mse(self):
        
        self.connection = psycopg2.connect(**self._config)
        self.connection.autocommit = True
        self.cursor = self.connection.cursor()
        
        query = f"""
            SELECT
                date
                ,close
                ,predicted
            FROM
                lb_tickers_data
            ORDER BY
                date 
        """
        try:
            self.cursor.execute(query)
            results = self.cursor.fetchall()
            
            results = [{
                "date" : item[0]
                ,"close" : item[1]
                ,"predicted" : item[2]
            } for item in results]
            
            return results
            
        except Exception as e:
            print(f"Erro ao buscada dados do ticker: {e}")
        finally:
            self.close_connection()
    
    def get_data_to_data_drift(self):
        
        self.connection = psycopg2.connect(**self._config)
        self.connection.autocommit = True
        self.cursor = self.connection.cursor()
        
        query_trianing = f"""
            SELECT
                date
                ,close
                ,predicted
            FROM
                lb_tickers_data
            WHERE
                is_training
            ORDER BY
                date 
        """
        
        query_prod = f"""
            SELECT
                date
                ,close
                ,predicted
            FROM
                lb_tickers_data
            WHERE
                not is_training
            ORDER BY
                date 
        """
        try:
            
            
            self.cursor.execute(query_trianing)
            results_training = self.cursor.fetchall()
            
            self.cursor.execute(query_prod)
            results_prod = self.cursor.fetchall()
            
            training = [{
                "date" : item[0]
                ,"close" : item[1]
                ,"predicted" : item[2]
            } for item in results_training]
            
            prod = [{
                "date" : item[0]
                ,"close" : item[1]
                ,"predicted" : item[2]
            } for item in results_prod]
            
            return training, prod
        
            
        except Exception as e:
            print(f"Erro ao buscada dados do ticker: {e}")
        finally:
            self.close_connection()