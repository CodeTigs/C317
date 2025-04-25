import psycopg2

try:
    conn = psycopg2.connect(
        dbname="orcamentos_db",
        user="postgres",
        password="Senha647",
        host="localhost",
        port="5432"
    )
    print("Conexão bem-sucedida!")
    conn.close()
except Exception as e:
    print("Erro na conexão:", e)
