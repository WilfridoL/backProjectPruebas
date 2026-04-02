from flask import Blueprint
from controllers.categoria_controller import cnlistado_categoria

categoria_bp = Blueprint('categoria', __name__)

@categoria_bp.route('/', methods=['GET'])
def listado():
    return cnlistado_categoria()