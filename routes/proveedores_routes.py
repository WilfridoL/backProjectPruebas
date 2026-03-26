from flask import Blueprint, jsonify
from services.proveedor_service import listado_proveedor

proveedor_bp = Blueprint('proveedor', __name__)

@proveedor_bp.route('/proveedores', methods=['GET'])
def get_proveedores():
    data = listado_proveedor()
    return jsonify(data)