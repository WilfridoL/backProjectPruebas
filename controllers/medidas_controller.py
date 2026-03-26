from flask import jsonify, request
from services.medidas_services import listado_medidas

def cnlistado_medidas():
    data = listado_medidas()
    return jsonify(data)
