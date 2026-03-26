from flask import jsonify, request
from services.tipo_prenda_services import listado_tipo_prenda

def cnlistado_tipo_prenda():
    data = listado_tipo_prenda()
    return jsonify(data)
