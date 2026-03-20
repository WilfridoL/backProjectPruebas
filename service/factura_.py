from flack import current_app
from models.factura import Factura
def listado_factura():
    c=current_app.msql.connection.cursor()
    sql="SELECT * FROM factura"
    c.execute(sql)
    data=c.fetchall()
    # los datos se convierten a diccionario
    return data
def buscarXid(id):
    c=current_app.msql.connection.cursor()
    sql="SELECT * FROM factura WHERE id=%s"
    c.execute(sql, (id,))
    data=c.fetchone()
    return data
def crear_factura():
    return
def eliminar_factura():
    return