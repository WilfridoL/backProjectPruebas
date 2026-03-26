from flask import Blueprint, jsonify
from services.venta_service import listado_ventas

venta_bp = Blueprint('ventas', __name__)

@venta_bp.route('/ventas', methods=['GET'])
def get_ventas():
    data = listado_ventas()
    return jsonify(data)