from flask import jsonify, request
from services.det_pedido_services import regDetallePedido

def cnRegistroDetalles(id):
    data = request.json

    # 🔒 Validar JSON
    if not data:
        return jsonify({"error": "Se requiere un body en formato JSON"}), 400

    # 🔒 Campos obligatorios
    campos_obligatorios = ["cantidad", "precio", "nombre"]

    faltantes = [c for c in campos_obligatorios if c not in data or data[c] is None]

    if faltantes:
        return jsonify({
            "error": "Faltan campos obligatorios",
            "faltantes": faltantes
        }), 400

    try:
        # ✅ Llamar al servicio
        respuesta = regDetallePedido(
            id=data.get("id"),  # o puedes generarlo
            id_pedido=id,       # 👈 viene de la URL /pedidos/<id>/detalles
            cantidad=data["cantidad"],
            precio=data["precio"],
            nombre=data["nombre"],
            tipo_prenda=data.get("tipo_prenda"),
            talla=data.get("talla"),
            observacion=data.get("observacion"),
            medidas=data.get("medidas")  # puede ser None o array
        )

        return jsonify({
            "message": "Detalle registrado con éxito",
            "data": respuesta
        }), 201

    except Exception as e:
        return jsonify({
            "error": str(e)
        }), 500
