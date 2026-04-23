from flask import current_app
from models.rol_model import Rol

def listado_roles():
    c=current_app.mysql.connection.cursor()
    sql="SELECT * FROM rol"
    c.execute(sql)
    data=c.fetchall()
    
    d = []
    for p in data:
        obj = Rol(
            id=p[0],
            nom=p[1],
            desc=p[2]
        ).toDic()
        d.append(obj)

    return d

# def crear_roles():
#     return
# def eliminar_roles():
#     return