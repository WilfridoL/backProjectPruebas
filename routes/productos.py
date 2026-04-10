from flask import Blueprint
from controllers.productos_controller import cnlistado_productos, cn_crear_producto

producto_bp = Blueprint("productos", __name__)

@producto_bp.route('/')
def listado():
    return cnlistado_productos()

@producto_bp.route('/', methods=['POST'])
def crear():
    return cn_crear_producto()