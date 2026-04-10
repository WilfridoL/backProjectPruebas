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
        # Validar que el ID no esté vacío
        if not cliId or not str(cliId).strip():
            raise ValueError("El ID del cliente es requerido")

        # Validar que nombre y apellido no estén vacíos
        if not cliNom or not cliNom.strip():
            raise ValueError("El nombre del cliente es requerido")
        if not cliApe or not cliApe.strip():
            raise ValueError("El apellido del cliente es requerido")

        # Validar que el teléfono solo tenga números
        if not str(cliTel).isdigit():
            raise ValueError("El teléfono solo debe contener números")

        # Validar longitud del teléfono
        if len(str(cliTel)) < 7 or len(str(cliTel)) > 15:
            raise ValueError("El teléfono debe tener entre 7 y 15 dígitos")

        # Validar que el usuId exista en la BD
        c = current_app.mysql.connection.cursor()
        c.execute("SELECT usuId FROM usuario WHERE usuId = %s", (usuId,))
        if not c.fetchone():
            raise ValueError(f"No existe un usuario con ID {usuId}")

        # Validar que el cliente no esté ya registrado
        c.execute("SELECT cliId FROM cliente WHERE cliId = %s", (cliId,))
        if c.fetchone():
            raise ValueError(f"Ya existe un cliente con ID {cliId}")

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

    except ValueError as ve:
        print(f"Validación fallida: {ve}")
        return False
    except Exception as e:
        print(e)
        return False