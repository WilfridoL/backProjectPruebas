from flask import jsonify, request
from services.pedido_foto_services import registrarFoto, eliminarFoto

def cnRegistrarFoto(id):
    data = request.json

    #  Validar JSON
    if not data:
        return jsonify({"error": "Se requiere un cuerpo JSON"}), 400

    #  Validar existencia del campo url
    if "url" not in data or data["url"] is None:
        return jsonify({"error": "Falta el campo 'url'"}), 400

    url = data["url"]

    #  Validar tipo de dato
    if not isinstance(url, str):
        return jsonify({"error": "La url debe ser un string"}), 400

    #  Validar que no esté vacía
    if not url.strip():
        return jsonify({"error": "La url no puede estar vacía"}), 400

    #  Validar longitud (opcional pero recomendado)
    if len(url) > 500:
        return jsonify({
            "error": "La url es demasiado larga (máx 500 caracteres)"
        }), 400

    try:
        respuesta = registrarFoto(id, url)

        return jsonify({
            "message": "Foto registrada correctamente",
            "data": respuesta
        }), 201

    except Exception as e:
        return jsonify({
            "error": str(e)
        }), 500

def cnEliminarFoto(id, id_pedido):
    return eliminarFoto(id, id_pedido)