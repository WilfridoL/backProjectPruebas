from flask import Blueprint, jsonify, request
from services.proveedores_services import (
    listado_proveedores,
    crear_proveedor,
    eliminar_proveedor,
    actualizar_proveedor
)

proveedor_bp = Blueprint('proveedor_bp', __name__)

@proveedor_bp.route('/', methods=['GET'])
def cnlistado_proveedores():
    return jsonify(listado_proveedores())

@proveedor_bp.route('/', methods=['POST'])
def cncrear_proveedor():
    data = request.json
    return jsonify({"ok": crear_proveedor(data)})

@proveedor_bp.route('/<string:id>', methods=['DELETE'])
def cneliminar_proveedor(id):
    return jsonify({"ok": eliminar_proveedor(id)})

@proveedor_bp.route('/<string:id>', methods=['PUT'])
def cnactualizar_proveedor(id):
    data = request.json
    return jsonify({"ok": actualizar_proveedor(id, data)})