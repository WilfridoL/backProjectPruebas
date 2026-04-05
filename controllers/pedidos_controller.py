from flask import jsonify, request
from services.pedido_services import listarPedidos, regPedidos, delPedido

def cntListadopedido():
    datos = listarPedidos()
    print(datos)
    return datos

def cntRegistrarPedido ():
    data = request.json

    if not data:
        return jsonify({"error": "Se requiere un cuerpo JSON"}), 400

    campos_obligatorios = ["id", "id_cliente", "tipo_pedido"]

    faltantes = [campo for campo in campos_obligatorios if campo not in data or data[campo] is None]

    if faltantes:
        return jsonify({
            "error": "Faltan campos obligatorios",
            "faltantes": faltantes
        }), 400

    id = data["id"]
    id_cliente = data["id_cliente"]
    tipo_pedido = data["tipo_pedido"]

    fecha_estimada = data.get("fecha_estimada")
    dias_recordatorio = data.get("dias_recordatorio") or 3
    precio_total_estimado = data.get("precio_total_estimado")
    observacion = data.get("observacion")

    regPedidos(
        id,
        id_cliente,
        tipo_pedido,
        fecha_estimada,
        dias_recordatorio,
        precio_total_estimado,
        observacion
    )

    return jsonify({
        "message": "registro con exito",
        "data": data
    })

def cntCancelarPedido(id):
    return delPedido(id)