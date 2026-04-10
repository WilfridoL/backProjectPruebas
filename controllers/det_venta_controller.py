from flask import jsonify, request
from services.det_venta_servies import listado_det_venta, registrarDetalleVenta, eliminarDetalleVenta


def cnlistado_det_venta():
    data=listado_det_venta()
    return jsonify(data)

def cntRegistrarDetalle(id_venta):
    data = request.json

    if not data:
        return jsonify({"error": "Se requiere un body en formato JSON"}), 400

    campos_obligatorios = ["id_producto", "cantidad", "precio"]
    faltantes = [c for c in campos_obligatorios if c not in data or data[c] is None]

    if faltantes:
        return jsonify({
            "error": "Faltan campos obligatorios",
            "faltantes": faltantes
        }), 400

    try:
        respuesta = registrarDetalleVenta(
            id_venta=id_venta,
            id_producto=data["id_producto"],
            cantidad=data["cantidad"],
            precio=data["precio"]
        )

        if "error" in respuesta:
            return jsonify(respuesta), 400

        return jsonify(respuesta), 201

    except Exception as e:
        return jsonify({"error": str(e)}), 500


def cntEliminarDetalle(id_detalle):
    try:
        respuesta = eliminarDetalleVenta(id_detalle)
        if "error" in respuesta:
            return jsonify(respuesta), 400
        return jsonify(respuesta), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
