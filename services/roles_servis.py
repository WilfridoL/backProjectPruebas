from flask import current_app
from models.rol_model import roles

def listado_roles():
    c=current_app.msql.connection.cursor()
    sql="SELECT * FROM roles"
    c.execute(sql)
    data=c.fetchall()
    return data
def crear_roles():
    return
def eliminar_roles():
    return