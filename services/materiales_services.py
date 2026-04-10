from flask import current_app
from models.materiales_model import materiales

def listado_materiales():
    c = current_app.mysql.connection.cursor()
    sql = "SELECT * FROM materiales"
    c.execute(sql)
    data = c.fetchall()
    d = []
    for m in data:
        obj = materiales(
            matId=m[0], matNom=m[1], matEst=m[2], matDesc=m[3],
            matUmbMin=m[4], matCantDisp=m[5], matUniMed=m[6],
            matPreUni=m[7], matProv=m[8], matTipMat=m[9]
        ).toDic()
        d.append(obj)
    return d

def crear_material(data):
    c = current_app.mysql.connection.cursor()
    sql = """
        INSERT INTO materiales 
        (matNom, matEst, matDesc, matUmbMin, matCantDisp, matUniMed, matPreUni, matProv, matTipMat)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
    """
    valores = (
        data['matNom'], data['matEst'], data.get('matDesc'),
        data['matUmbMin'], data['matCantDisp'], data.get('matUniMed'),
        data['matPreUni'], data.get('matProv'), data['matTipMat']
    )
    c.execute(sql, valores)
    current_app.mysql.connection.commit()
    return c.lastrowid, None