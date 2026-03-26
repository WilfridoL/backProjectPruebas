from flask import current_app
from models.venta_model import Venta

def listado_ventas():
    c = current_app.mysql.connection.cursor()
    sql = "SELECT * FROM ventas"
    c.execute(sql)
    data = c.fetchall()
    
    d = []
    for p in data:
        obj = Venta(
            venID=p[0],
            venFec=p[1],
            venDesc=p[2],
            estadoPago=p[3],
            venTotal=p[4],
            cliIdFk=p[5],
            usuIdFk=p[6],
            pedIdFk=p[7]
        ).toDic()
        d.append(obj)
    
    return d