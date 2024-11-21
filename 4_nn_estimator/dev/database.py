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

