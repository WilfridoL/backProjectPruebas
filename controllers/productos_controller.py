from  flask import jsonify, request
from services.factura_services import listado_productos, buscarXid


def cnlistado_productos():
    data=listado_productos()
    print(data)