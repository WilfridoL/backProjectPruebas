from flask import Blueprint
from controllers.cliente_controller import cnlistado_cliente, cnRegistrar_cliente

cliente_bp = Blueprint("cliente", __name__)

@cliente_bp.route('/')
def listado():
    return cnlistado_cliente()

@cliente_bp.route('/', methods=["POST"])
def registrar():
    return cnRegistrar_cliente()