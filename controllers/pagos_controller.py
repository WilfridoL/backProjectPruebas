from flask import jsonify, request
from services.pagos_services import listado_pagos

def cnlistado_pagos():
    data = listado_pagos()
    return jsonify(data)
