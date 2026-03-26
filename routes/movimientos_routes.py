from flask import Blueprint, jsonify
from services.movimiento_service import listado_movimientos

movimiento_bp = Blueprint('movimientos', __name__)

@movimiento_bp.route('/movimientos', methods=['GET'])
def get_movimientos():
    data = listado_movimientos()
    return jsonify(data)