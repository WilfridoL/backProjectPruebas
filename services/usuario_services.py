from flask import current_app
from models.usuario_model import usuario

def listarUsuario():
    c = current_app.mysql.connection.cursor()
    sql = "SELECT * FROM usuario"
    c.execute(sql)
    datos = c.fetchall()
    return datos