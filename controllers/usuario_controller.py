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

    # Validaciones
    if not data:
        return jsonify({"mensaje": "No se enviaron datos"}), 400

    campos_requeridos = ["usuId", "usuNom", "usuApe", "usuTel", "usuCor", "usuPassHash", "usuRol"]
    faltantes = [c for c in campos_requeridos if not data.get(c)]
    if faltantes:
        return jsonify({"mensaje": "Campos requeridos faltantes", "faltantes": faltantes}), 400

    resp = crear_usuario(data)

    if resp:
        return jsonify({"mensaje": "Usuario creado correctamente"})
    else:
        return jsonify({"mensaje": "Error al crear usuario"}), 500

# 🔹 ELIMINAR
def cneliminar_usuario(id):
    # Validaciones
    if not id or not id.strip():
        return jsonify({"mensaje": "ID no válido"}), 400

    resp = eliminar_usuario(id)

    if resp:
        return jsonify({"mensaje": "Usuario eliminado correctamente"})
    else:
        return jsonify({"mensaje": "Error al eliminar"}), 500

# 🔹 ACTUALIZAR
def cnactualizar_usuario(id):
    data = request.json

    # Validaciones
    if not id or not id.strip():
        return jsonify({"mensaje": "ID no válido"}), 400

    if not data:
        return jsonify({"mensaje": "No se enviaron datos"}), 400

    campos_requeridos = ["usuNom", "usuApe", "usuTel", "usuCor", "usuRol"]
    faltantes = [c for c in campos_requeridos if not data.get(c)]
    if faltantes:
        return jsonify({"mensaje": "Campos requeridos faltantes", "faltantes": faltantes}), 400

    resp = actualizar_usuario(id, data)

    if resp:
        return jsonify({"mensaje": "Usuario actualizado correctamente"})
    else:
        return jsonify({"mensaje": "Error al actualizar"}), 500