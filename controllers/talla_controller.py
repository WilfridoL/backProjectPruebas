from flask import jsonify, request
from services.talla_services import listado_talla

def cnlistado_talla():
    data = listado_talla()
    return jsonify(data)
