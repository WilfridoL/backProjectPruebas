from  flask import jsonify, request
from services.productos_services import listado_productos, crear_producto


def cnlistado_productos():
    data=listado_productos()
    # print(data)
    return jsonify(data)

def cn_crear_producto():
    data = request.get_json()
    campos = ['proId', 'proNom', 'proStock', 'proPreUni', 'proTipPro']
    for campo in campos:
        if not data or campo not in data or data[campo] == '':
            return jsonify({"error": f"El campo '{campo}' es obligatorio"}), 400

    resultado, error = crear_producto(data)
    if error:
        return jsonify({"error": error}), 409
    return jsonify({"mensaje": "Producto creado", "proId": resultado}), 201