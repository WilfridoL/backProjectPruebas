from flask import request, jsonify
from services.usuario_services import (
    listado_usuarios,
    crear_usuario,
    eliminar_usuario,
    actualizar_usuario
)

# 🔹 LISTAR
def cnlistado_usuarios():
    data = listado_usuarios()
    return jsonify(data)

# 🔹 CREAR
def cncrear_usuario():
    data = request.json
    resp = crear_usuario(data)

    if resp:
        return jsonify({"mensaje": "Usuario creado correctamente"})
    else:
        return jsonify({"mensaje": "Error al crear usuario"}), 500

# 🔹 ELIMINAR
def cneliminar_usuario(id):
    resp = eliminar_usuario(id)

    if resp:
        return jsonify({"mensaje": "Usuario eliminado correctamente"})
    else:
        return jsonify({"mensaje": "Error al eliminar"}), 500

# 🔹 ACTUALIZAR
def cnactualizar_usuario(id):
    data = request.json
    resp = actualizar_usuario(id, data)

    if resp:
        return jsonify({"mensaje": "Usuario actualizado correctamente"})
    else:
        return jsonify({"mensaje": "Error al actualizar"}), 500