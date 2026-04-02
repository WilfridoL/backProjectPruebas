from flask import Blueprint
from controllers.cliente_controller import cnlistado_cliente, cnRegistrar_cliente

cliente_bp = Blueprint('cliente_bp', __name__)

@cliente_bp.route('/clientes', methods=['GET'])
def listado_clientes():
    return cnlistado_cliente()

@cliente_bp.route('/clientes', methods=['POST'])
def registrar_cliente():
    return cnRegistrar_cliente()

