import psycopg2

def get_connection():
    return psycopg2.connect(
        dbname="orcamentos_db",
        user="postgres",
        password="Senha647",
        host="localhost",
        port="5432"
    )
