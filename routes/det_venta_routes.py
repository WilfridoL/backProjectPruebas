from flask import Blueprint, jsonify
from services.det_venta_servies import listado_det_venta

det_venta_bp = Blueprint('det_venta', __name__)

@det_venta_bp.route('/det-ventas', methods=['GET'])
def get_det_ventas():
    data = listado_det_venta()
    return jsonify(data)