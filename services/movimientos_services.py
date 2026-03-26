from flask import current_app
from models.movimiento_model import Movimiento

def listado_movimientos():
    c = current_app.mysql.connection.cursor()
    sql = "SELECT * FROM movimientos"
    c.execute(sql)
    data = c.fetchall()
    
    d = []
    for p in data:
        obj = Movimiento(
            idMov=p[0],
            tipo=p[1],
            cantidad=p[2],
            fecha=p[3],
            observacion=p[4],
            usuIdFk=p[5],
            proIdFk=p[6],
            matIdFk=p[7]
        ).toDic()
        d.append(obj)
    
    return d