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
            
    def get_data_tickers(self, from_date = None):
        
        self.connection = psycopg2.connect(**self._config)
        self.connection.autocommit = True
        self.cursor = self.connection.cursor()
        
        query = """
            SELECT 
                ticker
                ,open
                ,high
                ,low
                ,close
                ,volume
                ,date
            FROM
                lb_tickers_data
            order by
                date
            """
        
        if from_date is not None:
            query = f"""
            SELECT 
                ticker
                ,open
                ,high
                ,low
                ,close
                ,volume
                ,date
            FROM 
                lb_tickers_data
            WHERE
                cast(date as date) > cast('{from_date}' as date)
            ORDER BY
                date
            """        
        try:
            self.cursor.execute(query)
            results = self.cursor.fetchall()
            
            results = [{
                "ticker" : item[0]
                ,"open" : item[1]
                ,"high" : item[2]
                ,"low" : item[3]
                ,"close" : item[4]
                ,"volume" : item[5]
                ,"date" : item[6]
                } for item in results] 
            
            return results
        except Exception as e:
            print(f"Erro ao buscada dados do ticker: {e}")
        finally:
            self.close_connection()

