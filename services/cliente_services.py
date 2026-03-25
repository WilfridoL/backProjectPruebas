from flask import current_app
from models.cliente_model import Cliente

def listado_cliente():
    c = current_app.mysql.connection.cursor()
    sql="SELECT * FROM cliente"
    c.execute(sql)
    data=c.fetchall()
    d = []
    for p in data:
        obj = Cliente(
            cliId=p[0],
            cliNom=p[1],
            cliApe=p[2],
            cliTel=p[3],
            cliTel2=p[4],
            cliCorr=p[5],
            cliDir=p[6],
            usuFkID=p[7],
            cliEst=p[8],
            cliFecReg=p[9],
        ).toDic()
        d.append(obj)
    return d