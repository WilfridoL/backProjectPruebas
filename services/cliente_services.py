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


# =====================================================
# 🔹 CREAR CLIENTE
# =====================================================
def crear_cliente(data):
    try:
        c = current_app.mysql.connection.cursor()

        sql = """
        INSERT INTO cliente 
        (cliId, cliNom, cliApe, cliTel, cliTel2, cliCorr, cliDir, usuIdFk, cliEst)
        VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)
        """

        valores = (
            data['cliId'],
            data['cliNom'],
            data['cliApe'],
            data['cliTel'],
            data.get('cliTel2'),
            data.get('cliCorr'),
            data.get('cliDir'),
            data['usuIdFk'],
            data.get('cliEst', 1)
        )

        c.execute(sql, valores)
        current_app.mysql.connection.commit()

        return True

    except Exception as e:
        print(e)
        return False


# =====================================================
# 🔹 ELIMINAR CLIENTE (LÓGICO)
# =====================================================
def eliminar_cliente(id):
    try:
        c = current_app.mysql.connection.cursor()

        # 🔥 Eliminación lógica (mejor que borrar)
        sql = "UPDATE cliente SET cliEst = 2 WHERE cliId = %s"
        c.execute(sql, (id,))

        current_app.mysql.connection.commit()

        return True

    except Exception as e:
        print(e)
        return False


# =====================================================
# 🔹 ACTUALIZAR CLIENTE
# =====================================================
def actualizar_cliente(id, data):
    try:
        c = current_app.mysql.connection.cursor()

        sql = """
        UPDATE cliente 
        SET cliNom=%s, cliApe=%s, cliTel=%s, cliTel2=%s,
            cliCorr=%s, cliDir=%s, usuIdFk=%s
        WHERE cliId=%s
        """

        valores = (
            data['cliNom'],
            data['cliApe'],
            data['cliTel'],
            data.get('cliTel2'),
            data.get('cliCorr'),
            data.get('cliDir'),
            data['usuIdFk'],
            id
        )

        c.execute(sql, valores)
        current_app.mysql.connection.commit()

        return True

    except Exception as e:
        print(e)
        return False