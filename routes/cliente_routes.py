from flask import Blueprint
from controllers.cliente_controller import *

cliente_bp = Blueprint('cliente_bp', __name__)

cliente_bp.route('/clientes', methods=['GET'])(cnlistado_clientes)
cliente_bp.route('/clientes', methods=['POST'])(cncrear_cliente)
cliente_bp.route('/clientes/<string:id>', methods=['DELETE'])(cneliminar_cliente)
cliente_bp.route('/clientes/<string:id>', methods=['PUT'])(cnactualizar_cliente)