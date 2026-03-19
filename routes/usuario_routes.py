from flask import Blueprint
from controllers.usuario_controller import cntListadoUsuario

usuarios_bp = Blueprint("usuarios", __name__)

@usuarios_bp.route('/')
def listado():
    return cntListadoUsuario()