from flask import jsonify, request
from services.rol_services import listado_rol

def cnlistado_rol():
    data = listado_rol()
    return jsonify(data)