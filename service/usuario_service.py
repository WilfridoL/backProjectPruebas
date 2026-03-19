from flask import current_app
from models.usuario_model import usuario

def listarUsuario():
    cursor = current_app.mysql.connection.cursor()
    sql = "SELECT * FROM usuario"
    cursor.execute(sql)
    datos = cursor.fetchall()
    return datos