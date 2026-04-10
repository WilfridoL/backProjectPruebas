from flask import current_app
from models.proveedor_model import Proveedor

# =====================================================
# 🔹 LISTAR PROVEEDORES
# =====================================================
def listado_proveedores():
    c = current_app.mysql.connection.cursor()
    c.execute("SELECT * FROM proveedor")
    data = c.fetchall()

    d = []
    for p in data:
        obj = Proveedor(
            provId=p[0],
            provNom=p[1],
            provTel=p[2],
            provCorr=p[3],
            provDir=p[4]
        ).toDic()
        d.append(obj)

    return d



def crear_proveedor(data):
    try:
        c = current_app.mysql.connection.cursor()

        sql = """
        INSERT INTO proveedor
        (provId, provNom, provTel, provCorr, provDir)
        VALUES (%s,%s,%s,%s,%s)
        """

        valores = (
            data['provId'],
            data['provNom'],
            data.get('provTel'),
            data.get('provCorr'),
            data.get('provDir')
        )

        c.execute(sql, valores)
        current_app.mysql.connection.commit()

        return True

    except Exception as e:
        print(e)
        return False


# =====================================================
# 🔹 ELIMINAR PROVEEDOR
# =====================================================
def eliminar_proveedor(id):
    try:
        c = current_app.mysql.connection.cursor()

        sql = "DELETE FROM proveedor WHERE provId = %s"
        c.execute(sql, (id,))

        current_app.mysql.connection.commit()

        return True

    except Exception as e:
        print(e)
        return False


# =====================================================
# 🔹 ACTUALIZAR PROVEEDOR
# =====================================================
def actualizar_proveedor(id, data):
    try:
        c = current_app.mysql.connection.cursor()

        sql = """
        UPDATE proveedor 
        SET provNom=%s, provTel=%s, provCorr=%s, provDir=%s
        WHERE provId=%s
        """

        valores = (
            data['provNom'],
            data.get('provTel'),
            data.get('provCorr'),
            data.get('provDir'),
            id
        )

        c.execute(sql, valores)
        current_app.mysql.connection.commit()

        return True

    except Exception as e:
        print(e)
        return False