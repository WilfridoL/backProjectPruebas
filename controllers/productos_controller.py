from  flask import jsonify, request
from services.productos_services import listado_productos


def cnlistado_productos():
    data=listado_productos()
    # print(data)
    return jsonify(data)

def cnregistrar_producto():
    requerido = ['nombre', 'stock', 'preUni', 'desc', 'gen', 'catFk', 'tipPreFk', 'tipPro', 'umbMin', 'tallFk', 'provFk']
    faltantes = [ x for x in requerido if x not in request.json]
    if faltantes:
        return jsonify({"error": "Faltan campos requeridos", "campos": faltantes}), 400
    nombre = request.json['nombre']
    stock = request.json['stock']
    preUni = request.json['preUni']
    desc = request.json['desc']
    gen = request.json['gen']
    catFk = request.json['catFk']
    tipPreFk = request.json['tipPreFk']
    tipPro = request.json['tipPro']
    umbMin = request.json['umbMin']
    tallFk = request.json['tallFk']
    provFk = request.json['provFk']
    data = listado_productos().registrar(nombre, stock, preUni, desc, gen, catFk, tipPreFk, tipPro, umbMin, tallFk, provFk)
    return jsonify(data)
