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
        
        if '@' not in data.get('usuCor', ''):
            raise ValueError("Correo inválido")

       
        if not str(data.get('usuTel', '')).isdigit():
            raise ValueError("Teléfono inválido, solo números")

        if data.get('usuRol') not in [1, 2]:
            raise ValueError("Rol inválido, debe ser 1 o 2")

        if len(data.get('usuPassHash', '')) < 6:
            raise ValueError("La contraseña debe tener al menos 6 caracteres")

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
            data['usuPassHash'],  
            data['usuRol'],
            data.get('usuSupFk'),
            data.get('usuEst', 1)
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



def eliminar_usuario(id):
    try:
   
        c = current_app.mysql.connection.cursor()
        c.execute("SELECT usuId FROM usuario WHERE usuId = %s", (id,))
        if not c.fetchone():
            raise ValueError(f"No existe un usuario con ID {id}")

        sql = "UPDATE usuario SET usuEst = 2 WHERE usuId = %s"
        c.execute(sql, (id,))

        current_app.mysql.connection.commit()

        return True

    except ValueError as ve:
        print(f"Validación fallida: {ve}")
        return False
    except Exception as e:
        print(e)
        return False


def actualizar_usuario(id, data):
    try:
 
        c = current_app.mysql.connection.cursor()
        c.execute("SELECT usuId FROM usuario WHERE usuId = %s", (id,))
        if not c.fetchone():
            raise ValueError(f"No existe un usuario con ID {id}")

  
        if '@' not in data.get('usuCor', ''):
            raise ValueError("Correo inválido")

        if not str(data.get('usuTel', '')).isdigit():
            raise ValueError("Teléfono inválido, solo números")

       
        if data.get('usuRol') not in [1, 2]:
            raise ValueError("Rol inválido, debe ser 1 o 2")

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

    except ValueError as ve:
        print(f"Validación fallida: {ve}")
        return False
    except Exception as e:
        print(e)
        return False