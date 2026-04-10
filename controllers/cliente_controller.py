from  flask import jsonify, request
from services.cliente_services import listado_cliente


def cnlistado_cliente():
    return jsonify(listado_clientes())

def cnRegistrar_cliente():
    payload = request.json or {}
    required = ["cliId", "cliNom", "cliApe", "cliTel", "usuIdFk"]  # ← corregido
    missing = [f for f in required if f not in payload]
    if missing:
        return jsonify({"mensaje": "Campos faltantes", "faltantes": missing}), 400

    success = agregar_cliente(
        payload["cliId"],
        payload["cliNom"],
        payload["cliApe"],
        payload["cliTel"],
        payload["usuIdFk"]
    )

    if success:
        return jsonify({"mensaje": "Cliente registrado con éxito"}), 201
    else:
        return jsonify({"mensaje": "Error al crear cliente"}), 500