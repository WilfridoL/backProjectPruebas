from  flask import jsonify, request
from services.cliente_services import listado_cliente, agregar_cliente


def cnlistado_cliente():
    data=listado_cliente()
    return jsonify(data)

def cnRegistrar_cliente():
    # requerido = ["cliId", "cliNom", "cliApe", "cliTel", "usuId"]
    # resultado = [x for x in requerido if not in request.json[]]
    print(request.json)
    agregar_cliente(
        request.json["id"],
        request.json["nombre"],
        request.json["apellido"],
        request.json["telefono"],
        request.json["usuId"]

    )
    return jsonify({
        "message": "registro con exito",
        "data": request.json
    })