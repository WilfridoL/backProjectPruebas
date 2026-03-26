from flask import current_app
from models.det_venta_model import DetVenta

def listado_det_venta():
    c = current_app.mysql.connection.cursor()
    sql = "SELECT * FROM det_venta"
    c.execute(sql)
    data = c.fetchall()
    
    d = []
    for p in data:
        obj = DetVenta(
            detVenId=p[0],
            idVenta=p[1],
            idProFk=p[2],
            cantidad=p[3],
            precio=p[4],
            subtotal=p[5]
        ).toDic()
        d.append(obj)
    
    return d