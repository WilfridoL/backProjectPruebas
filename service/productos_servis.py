from flack import current_app
from models.producto_model import producto
def listado_productos():
    c=current_app.msql.connection.cursor()
    sql="SELECT * FROM producto"
    c.execute(sql)
    data=c.fetchall()
    # los datos se convierten a diccionario
    return data
def buscarXid(id):
    return