from flask import jsonify, request
from services.roles_services import listado_roles

def cnlistado_rol():
    data = listado_roles()
    return jsonify(data)