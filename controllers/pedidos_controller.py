from flask import jsonify, request
from services.pedido_services import listarPedidos, regPedidos, delPedido, listarUnPedido
from datetime import datetime

def cntListadopedido():
    datos = listarPedidos()
    print(datos)
    return datos

def cntListarPedidoPorId(id):
    return listarUnPedido(id)


def cntRegistrarPedido():
    data = request.json

    #  Validar JSON
    if not data:
        return jsonify({"error": "Se requiere un cuerpo JSON"}), 400

    #  Campos obligatorios
    campos_obligatorios = ["id", "id_cliente", "tipo_pedido"]

    faltantes = [campo for campo in campos_obligatorios if campo not in data or data[campo] is None]

    if faltantes:
        return jsonify({
            "error": "Faltan campos obligatorios",
            "faltantes": faltantes
        }), 400

    #  Extraer datos
    id = data["id"]
    id_cliente = data["id_cliente"]
    tipo_pedido = data["tipo_pedido"]

    fecha_estimada = data.get("fecha_estimada")
    dias_recordatorio = data.get("dias_recordatorio") or 3
    precio_total_estimado = data.get("precio_total_estimado")
    observacion = data.get("observacion")

    #  Validar ID (máx 5 caracteres)
    if not isinstance(id, str) or len(id) > 5:
        return jsonify({
            "error": "El 'id' debe ser string de máximo 5 caracteres"
        }), 400

    #  Validar id_cliente
    if not isinstance(id_cliente, str) or not id_cliente.strip():
        return jsonify({
            "error": "El 'id_cliente' debe ser un string no vacío"
        }), 400

    #  Validar tipo_pedido (ENUM)
    tipos_validos = ['PERSONALIZADO','RETOQUES','MODIFICACIONES']

    if tipo_pedido not in tipos_validos:
        return jsonify({
            "error": "tipo_pedido inválido",
            "valores_permitidos": tipos_validos
        }), 400

    #  Validar fecha_estimada (opcional)
    if fecha_estimada is not None:
        try:
            datetime.strptime(fecha_estimada, "%Y-%m-%d")
        except ValueError:
            return jsonify({
                "error": "fecha_estimada debe tener formato YYYY-MM-DD"
            }), 400

    #  Validar dias_recordatorio
    if not isinstance(dias_recordatorio, int) or dias_recordatorio < 0:
        return jsonify({
            "error": "dias_recordatorio debe ser un entero positivo"
        }), 400

    #  Validar precio_total_estimado
    if precio_total_estimado is not None:
        if not isinstance(precio_total_estimado, (int, float)) or precio_total_estimado < 0:
            return jsonify({
                "error": "precio_total_estimado debe ser numérico y mayor o igual a 0"
            }), 400

    #  Validar observacion
    if observacion is not None:
        if not isinstance(observacion, str):
            return jsonify({
                "error": "observacion debe ser un string"
            }), 400

    try:
        respuesta = regPedidos(
            id,
            id_cliente,
            tipo_pedido,
            fecha_estimada,
            dias_recordatorio,
            precio_total_estimado,
            observacion
        )

        return jsonify({
            "message": "Registro con éxito",
            "data": respuesta
        }), 201

    except Exception as e:
        return jsonify({
            "error": str(e)
        }), 500

def cntCancelarPedido(id):
    return delPedido(id)