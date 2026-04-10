from flask import Blueprint
from controllers.factura_controller import cnlistado_factura, cnCrearFactura, cnEliminarFactura

factura_bp = Blueprint('factura', __name__)

@factura_bp.route('/')
def listado():
    return cnlistado_factura()

@factura_bp.route('/', methods=['POST'])
def crear():
    return cnCrearFactura()

@factura_bp.route('/<string:id>', methods=['DELETE'])
def eliminar(id):
    return cnEliminarFactura(id)
