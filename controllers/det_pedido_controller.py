from flask import jsonify, request
from services.det_pedido_services import regDetallePedido, deleteDetPedido

def cnRegistroDetalles(id):
    data = request.json

    #  Validar JSON
    if not data:
        return jsonify({"error": "Se requiere un body en formato JSON"}), 400

    #  Campos obligatorios
    campos_obligatorios = ["id", "cantidad", "precio", "nombre"]

    faltantes = [c for c in campos_obligatorios if c not in data or data[c] is None]

    if faltantes:
        return jsonify({
            "error": "Faltan campos obligatorios",
            "faltantes": faltantes
        }), 400

    #  Validar ID (máx 5 caracteres)
    if not isinstance(data["id"], str) or len(data["id"]) > 5:
        return jsonify({
            "error": "El campo 'id' debe ser un string de máximo 5 caracteres"
        }), 400

    #  Validar cantidad (int)
    if not isinstance(data["cantidad"], int):
        return jsonify({
            "error": "El campo 'cantidad' debe ser un número entero"
        }), 400

    if data["cantidad"] <= 0:
        return jsonify({
            "error": "La cantidad debe ser mayor a 0"
        }), 400

    #  Validar precio (int o float)
    if not isinstance(data["precio"], (int, float)):
        return jsonify({
            "error": "El campo 'precio' debe ser numérico (int o float)"
        }), 400

    if data["precio"] <= 0:
        return jsonify({
            "error": "El precio debe ser mayor a 0"
        }), 400

    #  Validar nombre
    if not isinstance(data["nombre"], str) or not data["nombre"].strip():
        return jsonify({
            "error": "El campo 'nombre' debe ser un string no vacío"
        }), 400

    #  datos tipo ENUMS 
    tipos_prenda_validos = ['CAMISA','PANTALON','FALDA','ZAPATO','MEDIA','UNIFORME','MEDIAS']
    tallas_validas = ['XS','S','M','L','XL','XXL']

    #  Validar tipo_prenda 
    tipo_prenda = data.get("tipo_prenda")
    if tipo_prenda is not None:
        if tipo_prenda.upper() not in tipos_prenda_validos:
            return jsonify({
                "error": "tipo_prenda inválido",
                "valores_permitidos": tipos_prenda_validos
            }), 400

    #  Validar talla 
    talla = data.get("talla")
    if talla is not None:
        if talla.upper() not in tallas_validas:
            return jsonify({
                "error": "talla inválida",
                "valores_permitidos": tallas_validas
            }), 400

    #  Validar medidas
    medidas = data.get("medidas")
    if medidas is not None and not isinstance(medidas, list):
        return jsonify({
            "error": "El campo 'medidas' debe ser un arreglo"
        }), 400

    try:
        #  Llamar al servicio
        respuesta = regDetallePedido(
            id=data["id"],
            id_pedido=id,
            cantidad=data["cantidad"],
            precio=data["precio"],
            nombre=data["nombre"],
            tipo_prenda=tipo_prenda,
            talla=talla,
            observacion=data.get("observacion"),
            medidas=medidas
        )

        return jsonify({
            "message": "Detalle registrado con éxito",
            "data": respuesta
        }), 201

    except Exception as e:
        return jsonify({
            "error": str(e)
        }), 500

def cnDelete(id):
    return jsonify(deleteDetPedido(id))