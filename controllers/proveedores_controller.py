from flask import jsonify, request
from services.proveedores_services import listado_proveedores
def cnlistado_proveedores():
    data=listado_proveedores()
    return jsonify(data)
