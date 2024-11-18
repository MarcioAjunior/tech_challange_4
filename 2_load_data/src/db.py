import psycopg2
from psycopg2.extras import RealDictCursor

class PostgresSingleton:
    _instance = None 

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self, db_config=None): 
        if not hasattr(self, "_connection"):
            if not db_config:
                raise ValueError("Não foi encontrada configuração so DB")
            self._connection = psycopg2.connect(
                user=db_config["user"],
                password=db_config["password"],
                host=db_config["host"],
                port=db_config["port"],
                database=db_config["database"]
            )

    def execute_query(self, query, params=None):
        with self._connection.cursor(cursor_factory=RealDictCursor) as cursor:
            cursor.execute(query, params)
            if cursor.description:
                return cursor.fetchall()
            self._connection.commit()            
            return None
