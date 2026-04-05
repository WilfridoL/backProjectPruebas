from flask import jsonify, request
from services.pedido_foto_services import registrarFoto, eliminarFoto

def cnRegistrarFoto(id):
    data = request.json
    if not data:
        return jsonify({"error": "Se requiere un cuerpo JSON"}), 400
    
    if data["url"] is None:
        return jsonify({"error": "Falta la url"}), 400
    
    # return data
    return registrarFoto(id, str(data["url"]))

def cnEliminarFoto(id, id_pedido):
    return eliminarFoto(id, id_pedido)