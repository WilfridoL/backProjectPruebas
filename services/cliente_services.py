from flask import current_app
from models.cliente_model import Cliente

def listado_cliente():
    c=current_app.msql.connection.cursor()
    sql="SELECT * FROM cliente"
    c.execute(sql)
    data=c.fetchall()
    d = []
    for p in data:
        obj = Cliente(
            id=p[0],
            nom=p[1],
            ape=p[2],
            tel=p[3],
            tel2=p[4],
            corr=p[5],
            dir=p[6],
            usufk=p[7],
            est=p[8]
        ).toDic()
        d.append(obj)
    return d