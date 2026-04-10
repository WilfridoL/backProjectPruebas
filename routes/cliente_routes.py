from flask import Blueprint
from controllers.cliente_controller import cnlistado_cliente, cnRegistrar_cliente

cliente_bp = Blueprint('cliente_bp', __name__)


cliente_bp.route('/', methods=['GET'])(cnlistado_cliente)
cliente_bp.route('/', methods=['POST'])(cnRegistrar_cliente)