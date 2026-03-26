from flask import jsonify, request
from services.estado_pedido_services import listado_estado_pedido

def cnlistado_estado_pedido():
    data = listado_estado_pedido()
    return jsonify(data)