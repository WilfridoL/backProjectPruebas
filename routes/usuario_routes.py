from flask import Blueprint
from controllers.usuario_controller import *

usuarios_bp = Blueprint('usuarios_bp', __name__)  # ← añade la 's'

usuarios_bp.route('/usuarios', methods=['GET'])(cnlistado_usuarios)
usuarios_bp.route('/usuarios', methods=['POST'])(cncrear_usuario)
usuarios_bp.route('/usuarios/<string:id>', methods=['DELETE'])(cneliminar_usuario)
usuarios_bp.route('/usuarios/<string:id>', methods=['PUT'])(cnactualizar_usuario)