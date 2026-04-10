from flask import Blueprint
from controllers.usuario_controller import *

usuarios_bp = Blueprint('usuarios_bp', __name__)  

usuarios_bp.route('/', methods=['GET'])(cnlistado_usuarios)
usuarios_bp.route('/', methods=['POST'])(cncrear_usuario)
usuarios_bp.route('/', methods=['DELETE'])(cneliminar_usuario)
usuarios_bp.route('/', methods=['PUT'])(cnactualizar_usuario)