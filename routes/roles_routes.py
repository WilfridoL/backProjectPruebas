from flask import Blueprint
from controllers.rol_controller import cnlistado_rol

rol_bp = Blueprint('roles', __name__)

@rol_bp.route('/', methods=['GET'])
def listado():
    return cnlistado_rol()