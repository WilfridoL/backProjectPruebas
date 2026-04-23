from flask import jsonify, request
from services.pagos_services import listado_pagos, crear_pago

def cnlistado_pagos():
    data = listado_pagos()
    return jsonify(data)

def cn_crear_pago():
    data = request.get_json()

    campos = ['pagId', 'pagVenIdFk', 'pagMon', 'pagMetPag', 'pagEst']
    for campo in campos:
        if not data or campo not in data or data[campo] == '':
            return jsonify({"error": f"El campo '{campo}' es obligatorio"}), 400

    resultado, error = crear_pago(data)
    if error:
        return jsonify({"error": error}), 409
    return jsonify({"mensaje": "Pago registrado", "pagId": resultado}), 201