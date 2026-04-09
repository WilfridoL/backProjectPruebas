from flask import current_app
from models.usuario_model import Usuario

def listado_usuarios():
    c = current_app.mysql.connection.cursor()
    c.execute("SELECT * FROM usuario")
    data = c.fetchall()

    d = []
    for p in data:
        obj = Usuario(
            usuId=p[0],
            usuNom=p[1],
            usuApe=p[2],
            usuTel=p[3],
            usuCor=p[4],
            usuPassHash=p[5],
            usuRol=p[6],
            usuSupFk=p[7],
            usuEst=p[8],
            usuFecReg=str(p[9])
        ).toDic()
        d.append(obj)

    return d


# =====================================================
# 🔹 CREAR USUARIO
# =====================================================
def crear_usuario(data):
    try:
        c = current_app.mysql.connection.cursor()

        sql = """
        INSERT INTO usuario
        (usuId, usuNom, usuApe, usuTel, usuCor, usuPassHash, usuRol, usuSupFk, usuEst)
        VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)
        """

        valores = (
            data['usuId'],
            data['usuNom'],
            data['usuApe'],
            data['usuTel'],
            data['usuCor'],
            data['usuPassHash'],  # ⚠️ luego puedes encriptar
            data['usuRol'],
            data.get('usuSupFk'),
            data.get('usuEst', 1)
        )

        c.execute(sql, valores)
        current_app.mysql.connection.commit()

        return True

    except Exception as e:
        print(e)
        return False


# =====================================================
# 🔹 ELIMINAR USUARIO (LÓGICO)
# =====================================================
def eliminar_usuario(id):
    try:
        c = current_app.mysql.connection.cursor()

        sql = "UPDATE usuario SET usuEst = 2 WHERE usuId = %s"
        c.execute(sql, (id,))

        current_app.mysql.connection.commit()

        return True

    except Exception as e:
        print(e)
        return False


# =====================================================
# 🔹 ACTUALIZAR USUARIO
# =====================================================
def actualizar_usuario(id, data):
    try:
        c = current_app.mysql.connection.cursor()

        sql = """
        UPDATE usuario 
        SET usuNom=%s, usuApe=%s, usuTel=%s, usuCor=%s,
            usuRol=%s, usuSupFk=%s
        WHERE usuId=%s
        """

        valores = (
            data['usuNom'],
            data['usuApe'],
            data['usuTel'],
            data['usuCor'],
            data['usuRol'],
            data.get('usuSupFk'),
            id
        )

        c.execute(sql, valores)
        current_app.mysql.connection.commit()

        return True

    except Exception as e:
        print(e)
        return False