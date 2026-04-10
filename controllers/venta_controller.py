from flask import jsonify, request
from services.venta_services import listado_ventas, registrarVenta, anularVenta
def cnlistado_venta():
    data=listado_ventas()
    return jsonify(data)


def cntRegistrarVenta():
    data = request.json

    if not data:
        return jsonify({"error": "Se requiere un body en formato JSON"}), 400

    campos_obligatorios = ["id_cliente", "id_usuario"]
    faltantes = [c for c in campos_obligatorios if c not in data or data[c] is None]

    if faltantes:
        return jsonify({
            "error": "Faltan campos obligatorios",
            "faltantes": faltantes
        }), 400

    estados_validos = ['PAGADO', 'ANULADO', 'ADELANTADO', 'SIN PAGAR']
    estado = data.get("estado_pago", "SIN PAGAR")

    if estado not in estados_validos:
        return jsonify({
            "error": f"estado_pago inválido. Valores permitidos: {estados_validos}"
        }), 400

    try:
        respuesta = registrarVenta(
            id_cliente=data["id_cliente"],
            id_usuario=data["id_usuario"],
            fecha=data.get("fecha"),
            descuento=data.get("descuento", 0),
            estado_pago=estado,
            id_pedido=data.get("id_pedido"),
            fecha_limite=data.get("fecha_limite")
        )

        if "error" in respuesta:
            return jsonify(respuesta), 400

        return jsonify(respuesta), 201

    except Exception as e:
        return jsonify({"error": str(e)}), 500


def cntAnularVenta(id):
    try:
        respuesta = anularVenta(id)
        if "error" in respuesta:
            return jsonify(respuesta), 400
        return jsonify(respuesta), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500