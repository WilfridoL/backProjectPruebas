from flask import Blueprint, jsonify
from controllers.proveedores_controller import cnlistado_proveedores

proveedor_bp = Blueprint('proveedor', __name__)

@proveedor_bp.route('/', methods=['GET'])
def get_proveedores():
    return cnlistado_proveedores()