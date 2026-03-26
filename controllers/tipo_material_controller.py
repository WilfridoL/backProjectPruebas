from flask import jsonify, request
from services.tipo_material_services import listado_tipo_material

def cnlistado_tipo_material():
    data = listado_tipo_material()
    return jsonify(data)
