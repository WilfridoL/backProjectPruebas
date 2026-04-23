from flask import Blueprint
from controllers.materiales_controller import cnlistado_materiales, cn_crear_material

materiales_bp = Blueprint('materiales', __name__)

@materiales_bp.route('/', methods=['GET'])
def listado():
    return cnlistado_materiales()

@materiales_bp.route('/', methods=['POST'])
def crear():
    return cn_crear_material()