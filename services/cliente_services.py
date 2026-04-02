from flask import current_app
from models.cliente_model import Cliente

# =====================================================
# 🔹 LISTAR CLIENTES
# =====================================================
def listado_clientes():
    c = current_app.mysql.connection.cursor()
    sql = "SELECT * FROM cliente"
    c.execute(sql)
    data = c.fetchall()

    d = []
    for p in data:
        obj = Cliente(
            cliId=p[0],
            cliNom=p[1],
            cliApe=p[2],
            cliTel=p[3],
            cliTel2=p[4],
            cliCorr=p[5],
            cliDir=p[6],
            usuIdFk=p[7],
            cliEst=p[8],
            cliFecReg=str(p[9])
        ).toDic()
        d.append(obj)

    return d


def listado_cliente():
    # compatibilidad con variantes previas
    return listado_clientes()


def agregar_cliente(cliId, cliNom, cliApe, cliTel, usuId):
    try:
        c = current_app.mysql.connection.cursor()
        sql = """
        INSERT INTO cliente (cliId, cliNom, cliApe, cliTel, usuIdFk, cliEst)
        VALUES (%s, %s, %s, %s, %s, %s)
        """
        valores = (
            cliId,
            cliNom,
            cliApe,
            cliTel,
            usuId,
            1
        )
        c.execute(sql, valores)
        current_app.mysql.connection.commit()
        return True
    except Exception as e:
        print(e)
        return False