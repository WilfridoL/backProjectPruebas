from flask import current_app
from models.historial_pedido_model import historial_pedido

def listado_historial_pedidos():
    c = current_app.mysql.connection.cursor()
    sql = "SELECT * FROM historial_pedido"
    c.execute(sql)
    data = c.fetchall()
    d = []
    for p in data:
        obj = historial_pedido(
            histId=p[0],
            pedIdFk=p[1],
            estadoAnterior=p[2],
            estadoNuevo=p[3],
            usuIdFk=p[4],
            hisFec=p[5]
        ).toDic()
        d.append(obj)
    return d