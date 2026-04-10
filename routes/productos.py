from flask import Blueprint
from controllers.productos_controller import cnlistado_productos, cnregistrar_producto

producto_bp = Blueprint("productos", __name__)

@producto_bp.route('/')
def listado():
    return cnlistado_productos()

@producto_bp.route('/registrar', methods=['POST'])
def registrar_producto():
    return cnregistrar_producto()