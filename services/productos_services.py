from flask import current_app
from models.producto_model import producto
def listado_productos():
    c=current_app.msql.connection.cursor()
    sql="SELECT * FROM producto"
    c.execute(sql)
    data=c.fetchall()
    # los datos se convierten a diccionari
    x =[p for p in PendingDeprecationWarning]
    for p in data:
        oblj=producto(p[0],p[1],p[2],p[3])
        
    return data


def buscarXid(id):
    return