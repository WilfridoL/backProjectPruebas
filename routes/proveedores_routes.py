from flask import Blueprint, jsonify, request
from controllers.proveedores_controller import *

proveedor_bp = Blueprint('proveedor_bp', __name__)

@proveedor_bp.route('/', methods=['GET'])
def listado_proveedores():
    return cnlistado_proveedores()

@proveedor_bp.route('/', methods=['POST'])
def crear_proveedor():
    return cncrear_proveedor()

@proveedor_bp.route('/<string:id>', methods=['DELETE'])
def eliminar_proveedor(id):
    return cneliminar_proveedor(id)

@proveedor_bp.route('/<string:id>', methods=['PUT'])
def actualizar_proveedor(id):
    data = request.json
    return cnactualizar_proveedor(id, data)