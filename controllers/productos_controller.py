from  flask import jsonify, request
from models.factura_services import listado_productos, buscarXid


def cnlistado_productos():
    data=listado_productos()
    print(data)