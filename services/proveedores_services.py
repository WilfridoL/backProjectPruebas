from flask import current_app
from models.proveedor_model import Proveedor

def listado_proveedor():
    c = current_app.mysql.connection.cursor()
    sql = "SELECT * FROM proveedor"
    c.execute(sql)
    data = c.fetchall()
    
    d = []
    for p in data:
        obj = Proveedor(
            provId=p[0],
            provNom=p[1],
            provTel=p[2],
            provCorr=p[3],
            provDir=p[4],
            proTipMatSum=p[5]
        ).toDic()
        d.append(obj)
    
    return d