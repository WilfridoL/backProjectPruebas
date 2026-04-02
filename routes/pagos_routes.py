from flask import Blueprint
from controllers.pagos_controller import cnlistado_pagos

pagos_bp = Blueprint('pagos', __name__)

@pagos_bp.route('/', methods=['GET'])
def listado():
    return cnlistado_pagos()