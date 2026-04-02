from flask import jsonify, request
from services.venta_services import listado_ventas
def cnlistado_venta():
    data=listado_ventas()
    return jsonify(data)


