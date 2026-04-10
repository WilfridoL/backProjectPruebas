from flask import request, jsonify
from services.proveedores_services import (
    listado_proveedores,    
    crear_proveedor,
    eliminar_proveedor,
    actualizar_proveedor
)


def cnlistado_proveedores():
    data = listado_proveedores()
    return jsonify(data)


def cncrear_proveedor():
    data = request.json
    if not data:
        return jsonify({"mensaje": "No se enviaron datos"}), 400

    
    campos_requeridos = ["provId", "provNom"]
    faltantes = [c for c in campos_requeridos if not data.get(c)]
    if faltantes:
        return jsonify({"mensaje": "Campos requeridos faltantes", "faltantes": faltantes}), 400

    
    if data.get("provTel") and not str(data["provTel"]).isdigit():
        return jsonify({"mensaje": "El teléfono solo debe contener números"}), 400


    if data.get("provCorr") and "@" not in data["provCorr"]:
        return jsonify({"mensaje": "El correo no tiene un formato válido"}), 400
    
    resp = crear_proveedor(data)

    if resp:
        return jsonify({"mensaje": "Proveedor creado correctamente"})
    else:
        return jsonify({"mensaje": "Error al crear proveedor"}), 500


def cneliminar_proveedor(id):

    if not id or not str(id).strip():
        return jsonify({"mensaje": "ID no válido"}), 400

    resp = eliminar_proveedor(id)

    if resp:
        return jsonify({"mensaje": "Proveedor eliminado correctamente"})
    else:
        return jsonify({"mensaje": "Error al eliminar"}), 500


def cnactualizar_proveedor(id):
   
    if not id or not str(id).strip():
        return jsonify({"mensaje": "ID no válido"}), 400

    data = request.json

    
    if not data:
        return jsonify({"mensaje": "No se enviaron datos"}), 400

    if not data.get("provNom"):
        return jsonify({"mensaje": "El nombre del proveedor es requerido"}), 400

   
    if data.get("provTel") and not str(data["provTel"]).isdigit():
        return jsonify({"mensaje": "El teléfono solo debe contener números"}), 400

    
    if data.get("provCorr") and "@" not in data["provCorr"]:
        return jsonify({"mensaje": "El correo no tiene un formato válido"}), 400

    resp = actualizar_proveedor(id, data)

    if resp:
        return jsonify({"mensaje": "Proveedor actualizado correctamente"})
    else:
        return jsonify({"mensaje": "Error al actualizar"}), 500