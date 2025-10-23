import psycopg2
from psycopg2 import sql


class Database:
    def __init__(self, host, database, user, password):
        self.host = host
        self.database = database
        self.user = user
        self.password = password
        self.connection = None
    
    def connect(self):
        try:
            self.connection = psycopg2.connect(
                host=self.host,
                database=self.database,
                user=self.user,
                password=self.password
            )
            print("Conexão com o banco de dados estabelecida.")
        except Exception as e:
            print(f"Erro ao conectar ao banco: {e}")
    
    def close(self):
        if self.connection:
            self.connection.close()
            print("Conexão com o banco de dados fechada.")
    
    def commitDB(self, query, params=None):
        try:
            with self.connection.cursor() as cursor:
                cursor.execute(query, params)
                self.connection.commit()
        except Exception as e:
            print(f"Erro ao executar query: {e}")
    
    def readDB(self, query, params=None):
        try:
            with self.connection.cursor() as cursor:
                cursor.execute(query, params)
                return cursor.fetchall()
        except Exception as e:
            print(f"Erro ao buscar dados: {e}")
            return None

