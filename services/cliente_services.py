from flask import current_app
from models.cliente_model import Cliente
def listado_cliente():
    c=current_app.msql.connection.cursor()
    sql="SELECT * FROM cliente"
    c.execute(sql)
    data=c.fetchall()
    # los datos se convierten a diccionario
    return data