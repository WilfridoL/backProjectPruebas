from flask import Blueprint, jsonify
from controllers.pedidos_controller import cntListadopedido, cntRegistrarPedido, cntCancelarPedido
from controllers.det_pedido_controller import cnRegistroDetalles, cnDelete
from controllers.pedido_foto_controller import cnRegistrarFoto, cnEliminarFoto

pedidos_bp = Blueprint("pedidos", __name__)

# Metodos para ruta /pedidos
@pedidos_bp.route('/')
def listado():
    return cntListadopedido()

@pedidos_bp.route('/', methods=['POST'])
def reg():
    return cntRegistrarPedido()

@pedidos_bp.route('/<string:id>', methods=['DELETE'])
def delete_pedido(id):
    return cntCancelarPedido(id)

# Metodos para ruta /pedidos/id_pedido/detalles
# @pedidos_bp.route('/<string:id>/detalles', methods=['GET'])
# def obtener_detalles(id):
#     return jsonify({"mensaje": f"Detalles del pedido {id}"})

@pedidos_bp.route('/<string:id>/detalles', methods=['POST'])
def registrar_detalle(id):
    return cnRegistroDetalles(id)

@pedidos_bp.route('/<string:pedido_id>/detalles/<string:detalle_id>', methods=['DELETE'])
def eliminar_detalle(pedido_id, detalle_id):
    return cnDelete(detalle_id)

# Metodos para ruta /pedidos/id_pedido/fotos
@pedidos_bp.route('/<string:pedido_id>/fotos', methods=['POST'])
def registrar_foto(pedido_id):
    return cnRegistrarFoto(pedido_id)

@pedidos_bp.route('/<string:pedido_id>/fotos/<int:id_foto>', methods=['DELETE'])
def eliminar_foto(pedido_id, id_foto):
    return cnEliminarFoto(id_foto, pedido_id)

# Metodos para ruta /pedidos/id_pedido/detalles/id_detalle/medidas
