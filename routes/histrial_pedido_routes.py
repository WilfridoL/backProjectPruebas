from flask import Blueprint
from controllers.historial_pedido_controller import cnlistado_historial_pedidos, cnlistado_historial_pedidos

historial_pedido_bp = Blueprint('historial_pedido', __name__)

@historial_pedido_bp.route('/', methods=['GET'])
def listado():
    return cnlistado_historial_pedidos()