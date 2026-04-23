from flask import Blueprint, jsonify
from controllers.venta_controller import ( cnlistado_venta,
    cntRegistrarVenta, cntAnularVenta)
from controllers.det_venta_controller import (
    cntRegistrarDetalle, cntEliminarDetalle
)

venta_bp = Blueprint('ventas', __name__)

@venta_bp.route('/', methods=['GET'])
def get_ventas():
    return cnlistado_venta()


@venta_bp.route('/', methods=['POST'])
def registrar():
    return cntRegistrarVenta()

@venta_bp.route('/<string:id>', methods=['DELETE'])
def anular(id):
    return cntAnularVenta(id)


@venta_bp.route('/<string:id_venta>/detalles', methods=['POST'])
def registrarDetalle(id_venta):
    return cntRegistrarDetalle(id_venta)

@venta_bp.route('/<string:id_venta>/detalles/<string:id_detalle>', methods=['DELETE'])
def eliminarDetalle(id_venta, id_detalle):
    return cntEliminarDetalle(id_detalle)
