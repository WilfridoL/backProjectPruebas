from flask import jsonify, request
from services.materiales_services import listado_materiales

def cnlistado_materiales():
    data = listado_materiales()
    return jsonify(data)
