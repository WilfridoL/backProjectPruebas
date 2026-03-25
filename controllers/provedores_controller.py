from flask import jsonify, request
from services.productos_services import listado_productos
def cnlistado_productos():
    data=listado_productos()
    print(data)
    return jsonify(data)