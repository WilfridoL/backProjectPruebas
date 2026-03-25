from flask import jsonify, request
from services.movimientos_services import listado_movimientos
def cnlistado_movimientos():
    data=listado_movimientos()
    return jsonify(data)