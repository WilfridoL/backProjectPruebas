from flask import Blueprint
from controllers.cliente_controller import cnlistado_cliente, cnRegistrar_cliente

cliente_bp = Blueprint('cliente_bp', __name__)

# ← sin redefinir funciones, directo al controlador
cliente_bp.route('/clientes', methods=['GET'])(cnlistado_cliente)
cliente_bp.route('/clientes', methods=['POST'])(cnRegistrar_cliente)