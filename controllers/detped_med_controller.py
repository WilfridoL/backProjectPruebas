from flask import jsonify, request
from services.detped_med_services import listado_detped_med

def cnlistado_detped_med():
    data = listado_detped_med()
    return jsonify(data)
