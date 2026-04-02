from flask import jsonify, request
from services.cliente_services import listado_clientes, agregar_cliente

# 🔹 LISTAR

def cnlistado_cliente():
    data = listado_clientes()
    return jsonify(data)


# 🔹 CREAR

def cnRegistrar_cliente():
    payload = request.json or {}
    required = ["id", "nombre", "apellido", "telefono", "usuId"]
    missing = [field for field in required if field not in payload]
    if missing:
        return jsonify({"mensaje": "Campos faltantes", "faltantes": missing}), 400

    success = agregar_cliente(
        payload["id"],
        payload["nombre"],
        payload["apellido"],
        payload["telefono"],
        payload["usuId"]
    )

    if success:
        return jsonify({"message": "registro con exito", "data": payload}), 201
    else:
        return jsonify({"message": "Error al crear cliente"}), 500

