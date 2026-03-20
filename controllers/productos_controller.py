from  flack import jsonify, request
from service.productos_servis import listado_productos, buscarXid


def cnlistado_productos():
    data=listado_productos()
    print(data)