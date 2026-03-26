from flask import jsonify, request
from services.factura_services import listado_factura

def cnlistado_factura():
    data = listado_factura()
    return jsonify(data)