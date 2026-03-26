from flask import jsonify, request
from services.det_venta_servies import listado_det_venta
def cnlistado_det_venta():
    data=listado_det_venta()
    return jsonify(data)