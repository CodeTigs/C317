import pandas as pd
from infra.database.db_config import get_connection

def importar_dados():
    conn = get_connection()
    cur = conn.cursor()

    df_usuarios = pd.read_csv("data/usuarios.csv", delimiter=";")
    df_precos = pd.read_csv("data/precos.csv", delimiter=";")
    df_orcamentos = pd.read_csv("data/orcamentos.csv", delimiter=";")

    for _, row in df_usuarios.iterrows():
        cur.execute("INSERT INTO base_usuario (id_usuario, nome, email, tipo_usuario, data_criacao) VALUES (%s, %s, %s, %s, %s)",
                    (row["id_usuario"], row["nome"], row["email"], row["tipo_usuario"], row["data_criacao"]))

    for _, row in df_precos.iterrows():
        cur.execute("INSERT INTO base_preco (id_preco, item, categoria, valor_unitario, data_atualizacao, criado_por) VALUES (%s, %s, %s, %s, %s, %s)",
                    (row["id_preco"], row["item"], row["categoria"], row["valor_unitario"], row["data_atualizacao"], row["criado_por"]))

    for _, row in df_orcamentos.iterrows():
        cur.execute("INSERT INTO orcamentos_salvos (id_orcamento, data_criacao, descricao, valor_total, status) VALUES (%s, %s, %s, %s, %s)",
                    (row["id_orcamento"], row["data_criacao"], row["descricao"], row["valor_total"], row["status"]))

    conn.commit()
    cur.close()
    conn.close()

if __name__ == "__main__":
    importar_dados()