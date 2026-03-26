from flask import Blueprint, jsonify
from controllers.venta_controller import cnlistado_venta

venta_bp = Blueprint('ventas', __name__)

@venta_bp.route('/', methods=['GET'])
def get_ventas():
    return cnlistado_venta()