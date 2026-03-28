from flask import current_app
from models.pagos_model import Det_venta

def listado_pagos():
    c = current_app.mysql.connection.cursor()
    sql = "SELECT * FROM pagos"
    c.execute(sql)
    data = c.fetchall()
    d = []
    for p in data:
        obj = Det_venta(
            id=p[0],
            idven=p[1],
            monto=p[2],
            metpago=p[3],
            pagFec=p[4],
            est=p[5]

        ).toDic()
        d.append(obj)
    return d