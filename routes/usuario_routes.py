from flask import Blueprint
from controllers.usuario_controller import cntListadoUsuario

usaurios_bp = Blueprint("usuario", __name__)
@usaurios_bp.route('/')
def listado():
    return cntListadoUsuario()