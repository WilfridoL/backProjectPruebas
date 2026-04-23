from flask import Blueprint
from controllers.pagos_controller import cnlistado_pagos, cn_crear_pago

pagos_bp = Blueprint('pagos', __name__)

@pagos_bp.route('/', methods=['GET'])
def listado():
    return cnlistado_pagos()

@pagos_bp.route('/', methods=['POST'])
def crear():
    return cn_crear_pago()