from flask import jsonify
from services.historial_pedido_services import listado_historial_pedidos

def cnlistado_historial_pedidos():
    data = listado_historial_pedidos()
    return jsonify(data)