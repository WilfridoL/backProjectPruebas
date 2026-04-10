from  flask import jsonify, request
from services.cliente_services import listado_clientes, agregar_cliente


def cnlistado_cliente():
    return jsonify(listado_clientes())

def cnRegistrar_cliente():
    payload = request.json or {}
    required = ["cliId", "cliNom", "cliApe", "cliTel", "usuIdFk"]
    missing = [f for f in required if f not in payload]
    if missing:
        return jsonify({"mensaje": "Campos faltantes", "faltantes": missing}), 400

    # ── Validaciones ──────────────────────────────────────────────
    cliId  = payload["cliId"]
    cliNom = payload["cliNom"].strip()
    cliApe = payload["cliApe"].strip()
    cliTel = payload["cliTel"].strip()
    usuIdFk = payload["usuIdFk"]

    if not isinstance(cliId, int) or cliId <= 0:
        return jsonify({"mensaje": "cliId debe ser un entero positivo"}), 400

    if not isinstance(usuIdFk, int) or usuIdFk <= 0:
        return jsonify({"mensaje": "usuIdFk debe ser un entero positivo"}), 400

    if not cliNom or not cliNom.replace(" ", "").isalpha():
        return jsonify({"mensaje": "cliNom solo debe contener letras y no estar vacío"}), 400

    if len(cliNom) > 100:
        return jsonify({"mensaje": "cliNom no puede superar los 100 caracteres"}), 400

    if not cliApe or not cliApe.replace(" ", "").isalpha():
        return jsonify({"mensaje": "cliApe solo debe contener letras y no estar vacío"}), 400

    if len(cliApe) > 100:
        return jsonify({"mensaje": "cliApe no puede superar los 100 caracteres"}), 400

    if not cliTel.isdigit():
        return jsonify({"mensaje": "cliTel solo debe contener dígitos"}), 400

    if not (7 <= len(cliTel) <= 15):
        return jsonify({"mensaje": "cliTel debe tener entre 7 y 15 dígitos"}), 400
    # ─────────────────────────────────────────────────────────────

    success = agregar_cliente(
        cliId,
        cliNom,
        cliApe,
        cliTel,
        usuIdFk
    )

    if success:
        return jsonify({"mensaje": "Cliente registrado con éxito"}), 201
    else:
        return jsonify({"mensaje": "Error al crear cliente"}), 500