from flask import jsonify, request
from services.tip_pedido_services import listado_tip_pedido

def cnlistado_tip_pedido():
    data = listado_tip_pedido()
    return jsonify(data)
