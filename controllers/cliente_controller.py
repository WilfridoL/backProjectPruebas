from  flask import jsonify, request
from flask import request, jsonify
from services.cliente_services import (
    listado_clientes,
    crear_cliente,
    eliminar_cliente,
    actualizar_cliente
)

# 🔹 LISTAR
def cnlistado_clientes():
    data = listado_clientes()
    return jsonify(data)

# 🔹 CREAR
def cncrear_cliente():
    data = request.json
    resp = crear_cliente(data)

    if resp:
        return jsonify({"mensaje": "Cliente creado correctamente"})
    else:
        return jsonify({"mensaje": "Error al crear cliente"}), 500

# 🔹 ELIMINAR
def cneliminar_cliente(id):
    resp = eliminar_cliente(id)

    if resp:
        return jsonify({"mensaje": "Cliente eliminado correctamente"})
    else:
        return jsonify({"mensaje": "Error al eliminar"}), 500

# 🔹 ACTUALIZAR
def cnactualizar_cliente(id):
    data = request.json
    resp = actualizar_cliente(id, data)

    if resp:
        return jsonify({"mensaje": "Cliente actualizado correctamente"})
    else:
        return jsonify({"mensaje": "Error al actualizar"}), 500