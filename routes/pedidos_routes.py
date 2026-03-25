from flask import Blueprint
from controllers.pedidos_controller import cntListadopedido

pedidos_bp = Blueprint("pedidos", __name__)

@pedidos_bp.route('/')
def listado():
    return cntListadopedido()