from flask import jsonify, request
from services.usuario_services import listarUsuario

def cntListadoUsuario():
    datos = listarUsuario()
    print(datos)
