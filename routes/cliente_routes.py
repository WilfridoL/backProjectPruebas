from flask import Blueprint
from controllers.cliente_controller import cnlistado_cliente

cliente_bp = Blueprint("cliente", __name__)

@cliente_bp.route('/')
def listado():
    return cnlistado_cliente