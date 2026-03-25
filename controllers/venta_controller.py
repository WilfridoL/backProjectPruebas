from flask import jsonify, request
from services.venta_services import listado_venta
def cnlistado_venta():
    data=listado_venta()
    return jsonify(data)