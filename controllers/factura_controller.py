from flask import jsonify, request
from services.factura_services import listado_factura, crear_factura, eliminar_factura

def cnlistado_factura():
    data = listado_factura()
    return jsonify(data)


def cnCrearFactura():
    data = request.json
    if not data:
        return jsonify({"error": "Se requiere un body en formato JSON"}), 400

    campos_obligatorios = ["facId", "facTotal", "numfactura"]
    faltantes = [c for c in campos_obligatorios if c not in data or data[c] is None]
    if faltantes:
        return jsonify({"error": "Faltan campos obligatorios", "faltantes": faltantes}), 400

    respuesta = crear_factura(
        facId=data["facId"],
        facTotal=data["facTotal"],
        numfatura=data["numfactura"],
        facFecEmi=data.get("facFecEmi")
    )

    if "error" in respuesta:
        return jsonify(respuesta), 400

    return jsonify(respuesta), 201


def cnEliminarFactura(id):
    respuesta = eliminar_factura(id)
    if "error" in respuesta:
        return jsonify(respuesta), 400
    return jsonify(respuesta), 200
