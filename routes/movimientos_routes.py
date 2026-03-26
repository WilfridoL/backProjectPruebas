from flask import Blueprint, jsonify
from controllers.movimientos_controller import cnlistado_movimientos

movimiento_bp = Blueprint('movimientos', __name__)

@movimiento_bp.route('/', methods=['GET'])
def get_movimientos():
    return cnlistado_movimientos()