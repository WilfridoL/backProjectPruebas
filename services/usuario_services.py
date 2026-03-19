from flask import current_app
from models.usuario_model import usuario

def listarUsuario():
    c = current_app.mysql.connection.cursor()
    sql = "SELECT * FROM usuario"
    c.execute(sql)
    datos = c.fetchall()
    d = []
    for p in datos:
        obj = usuario(
            usuId=p[0],
            usuNom=p[1],
            usuApe=p[2],
            usuTel=p[3],
            usuCor=p[4],
            usuPassHash=p[5],
            usuRol=p[6],
            usuSupFK=p[7],
            usuEst=p[8],
            usuFecReg=p[9]
        ).toDic()
        d.append(obj)
    return d