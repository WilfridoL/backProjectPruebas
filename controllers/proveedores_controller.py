from flask import jsonify, request
from services.proveedores_services import listado_proveedor
def cnlistado_proveedores():
    data=listado_proveedor()
    return jsonify(data)
