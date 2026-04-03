from flask import Blueprint, jsonify
from controllers.pedidos_controller import cntListadopedido, cntRegistrarPedido
from controllers.det_pedido_controller import cnRegistroDetalles

pedidos_bp = Blueprint("pedidos", __name__)

@pedidos_bp.route('/')
def listado():
    return cntListadopedido()

@pedidos_bp.route('/', methods=['POST'])
def reg():
    return cntRegistrarPedido()

@pedidos_bp.route('/<string:id>/detalles', methods=['GET'])
def obtener_detalles(id):
    return jsonify({"mensaje": f"Detalles del pedido {id}"})

@pedidos_bp.route('/<string:id>/detalles', methods=['POST'])
def obtener_detallesw(id):
    return cnRegistroDetalles(id)