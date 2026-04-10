from flask import request, jsonify
from services.proveedores_services import (
    listado_proveedores,    
    crear_proveedor,
    eliminar_proveedor,
    actualizar_proveedor
)

# 🔹 LISTAR
def cnlistado_proveedores():
    data = listado_proveedores()
    return jsonify(data)

# 🔹 CREAR
def cncrear_proveedor(data):
    resp = crear_proveedor(data)

    if resp:
        return jsonify({"mensaje": "Proveedor creado correctamente"})
    else:
        return jsonify({"mensaje": "Error al crear proveedor"}), 500

# 🔹 ELIMINAR
def cneliminar_proveedor(id):
    resp = eliminar_proveedor(id)

    if resp:
        return jsonify({"mensaje": "Proveedor eliminado correctamente"})
    else:
        return jsonify({"mensaje": "Error al eliminar"}), 500

# 🔹 ACTUALIZAR
def cnactualizar_proveedor(id):
    data = request.json
    resp = actualizar_proveedor(id, data)

    if resp:
        return jsonify({"mensaje": "Proveedor actualizado correctamente"})
    else:
        return jsonify({"mensaje": "Error al actualizar"}), 500