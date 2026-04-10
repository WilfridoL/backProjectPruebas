from flask import jsonify, request
from services.materiales_services import listado_materiales, crear_material

def cnlistado_materiales():
    data = listado_materiales()
    return jsonify(data)

def cn_crear_material():
    data = request.get_json()
    campos = ['matNom', 'matEst', 'matUmbMin', 'matCantDisp', 'matPreUni', 'matTipMat']
    for campo in campos:
        if not data or campo not in data or data[campo] == '':
            return jsonify({"error": f"El campo '{campo}' es obligatorio"}), 400

    resultado, error = crear_material(data)
    if error:
        return jsonify({"error": error}), 409
    return jsonify({"mensaje": "Material creado", "matId": resultado}), 201
