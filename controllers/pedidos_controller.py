from flask import jsonify, request
from services.pedido_services import listarPedidos

def cntListadopedido():
    datos = listarPedidos()
    print(datos)
    return datos
