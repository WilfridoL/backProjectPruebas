from flask import jsonify, request
from services.categoria_services import listado_categoria

def cnlistado_categoria():
    data = listado_categoria()
    return jsonify(data)