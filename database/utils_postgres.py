from infra.database.db_config import get_connection

class Utils:
    @staticmethod
    def buscar_usuario(id_usuario):
        conn = get_connection()
        cur = conn.cursor()
        cur.execute("SELECT * FROM base_usuario WHERE id_usuario = %s", (id_usuario,))
        usuario = cur.fetchone()
        cur.close()
        conn.close()
        return usuario

    @staticmethod
    def listar_precos_por_usuario(id_usuario):
        conn = get_connection()
        cur = conn.cursor()
        cur.execute("SELECT * FROM base_preco WHERE criado_por = %s", (id_usuario,))
        precos = cur.fetchall()
        cur.close()
        conn.close()
        return precos

    @staticmethod
    def listar_orcamentos():
        conn = get_connection()
        cur = conn.cursor()
        cur.execute("SELECT * FROM orcamentos_salvos")
        orcamentos = cur.fetchall()
        cur.close()
        conn.close()
        return orcamentos