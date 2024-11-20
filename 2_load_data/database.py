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

    def resgister_tickers_data(self, data_list):
        
        self.connection = psycopg2.connect(**self._config)
        self.connection.autocommit = True
        self.cursor = self.connection.cursor()
        
        query = """
        INSERT INTO lb_tickers_data (
            hash, ticker, date, open, high, low, close, price, volume
        ) VALUES %s
        ON CONFLICT (hash) DO NOTHING;
        """  
        values = [
            (
                item['hash'],
                item['ticker'],
                item['date'],
                item['open'],
                item['high'],
                item['low'],
                item['close'],
                item['price'],
                int(item['volume'])
            )
            for item in data_list
        ]

        try:
            execute_values(self.cursor, query, values)
            #print(f"{len(values)}")
            #print(f"{query}")
        except Exception as e:
            print(f"Erro ao inserir datas do tiker: {e}")
        finally:
            self.close_connection()
