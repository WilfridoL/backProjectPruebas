from flask import jsonify, request
from services.medidas_services import regMedidaPedido, eliminarMedidaEspecifica

# registrar medida
def cnRegistrar_medidas(id):
    data = request.json

    valor = data.get("valor")
    id_medida = data.get("id_medida")

    campos_obligatorios = ["valor", "id_medida"] #  Campos obligatorios

    faltantes = [c for c in campos_obligatorios if c not in data or data[c] is None]

    if faltantes:
        return jsonify({
            "error": "Faltan campos obligatorios",
            "faltantes": faltantes
        }), 400
    
    if not isinstance(valor, (int, float)): return jsonify({"error": "formato de valor incorrecto"}), 400 # si el valor no es de tipo numerico
    if valor <= 0: return jsonify({"error": "el valor no puede ser menor o igual a 0"}), 400 

    if not isinstance(id_medida, (int)): return jsonify({"error": "id_medida debe ser de tipo entero (int)."}), 400

    # print(type(id),type(valor), re.fullmatch(r'^\d+$', id_medida))
    return regMedidaPedido(id, id_medida, valor)

# eliminar medida
def cnEliminarMedida(id_medida, id_detalle):

    if not id_medida or not id_detalle:
        return jsonify({"error": "Los parámetros id_medida e id_detalle son obligatorios."}), 400

    if not str(id_medida).isdigit():
        return jsonify({"error": "El id_medida debe ser un número entero válido."}), 400

    try:
        id_medida = int(id_medida)
    except:
        return jsonify({"error": "Error al convertir los identificadores a número."}), 400

    if id_medida <= 0:
        return jsonify({"error": "El id_medida debe ser mayor que 0."}), 400


    return eliminarMedidaEspecifica(id_detalle, id_medida)