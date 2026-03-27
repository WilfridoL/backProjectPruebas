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

def agregar_cliente(
    id,
    nom,
    ape,
    tel,
    usuId,
    tel2 = None,
    corr = None,
    dir = None,
):
    c = current_app.mysql.connection.cursor()
    sql = """
    INSERT INTO cliente (cliId, cliNom, cliApe, cliTel, cliTel2, cliCorr, cliDir, usuIdFk)
    VALUE (%s, %s, %s, %s, %s, %s, %s, %s) 
    """

    c.execute(sql, id, nom, ape, tel, tel2, corr, dir, usuId)
    current_app.mysql.connection.commit()
    c.close()

