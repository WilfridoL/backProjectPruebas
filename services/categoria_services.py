from flask import current_app
from models.categoria_model import Categoria

def listado_categoria():
    c = current_app.mysql.connection.cursor()
    sql = "SELECT * FROM categoria"
    c.execute(sql)
    data = c.fetchall()
    d = []
    for p in data:
        obj = Categoria(
            id=p[0],
            nom=p[1],
            desc=p[2] if len(p) > 2 else None
        ).toDic()
        d.append(obj)
    return d
