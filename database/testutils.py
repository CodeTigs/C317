from infra.database.utils_postgres import Utils

usuario = Utils.buscar_usuario(1)
print("Usuário:", usuario)

precos = Utils.listar_precos_por_usuario(1)
print("Preços:", precos)

orcamentos = Utils.listar_orcamentos()
print("Orçamentos:", orcamentos)
