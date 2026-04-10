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


def crear_pago(data):
    c = current_app.mysql.connection.cursor()

    # Validar que el pagId no exista
    c.execute("SELECT pagId FROM pagos WHERE pagId = %s", (data['pagId'],))
    if c.fetchone():
        return None, "Ya existe un pago con ese ID"

    sql = """
        INSERT INTO pagos (pagId, pagVenIdFk, pagMon, pagMetPag, pagFec, pagEst)
        VALUES (%s, %s, %s, %s, %s, %s)
    """
    valores = (
        data['pagId'], data['pagVenIdFk'], data['pagMon'],
        data['pagMetPag'], data.get('pagFec'), data['pagEst']
    )
    c.execute(sql, valores)
    current_app.mysql.connection.commit()
    return data['pagId'], None