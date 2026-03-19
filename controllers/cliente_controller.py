from  flask import jsonify, request
from services.cliente_services import listado_cliente


def cnlistado_cliente():
    data=listado_cliente()
    return jsonify(data)