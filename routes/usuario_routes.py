from flask import Blueprint
from controllers.usuario_controller import *

usuario_bp = Blueprint('usuario_bp', __name__)

usuario_bp.route('/usuarios', methods=['GET'])(cnlistado_usuarios)
usuario_bp.route('/usuarios', methods=['POST'])(cncrear_usuario)
usuario_bp.route('/usuarios/<string:id>', methods=['DELETE'])(cneliminar_usuario)
usuario_bp.route('/usuarios/<string:id>', methods=['PUT'])(cnactualizar_usuario)