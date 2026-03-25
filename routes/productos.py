from flask import Blueprint
from controllers.productos_controller import cnlistado_productos

producto_bp = Blueprint("productos", __name__)

@producto_bp.route('/')
def listado():
    return cnlistado_productos()