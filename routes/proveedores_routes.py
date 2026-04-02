from flask import Blueprint
from controllers.proveedor_controller import (
    cnlistado_proveedores,
    cncrear_proveedor,
    cneliminar_proveedor,
    cnactualizar_proveedor
)

proveedor_bp = Blueprint('proveedor_bp', __name__)

proveedor_bp.route('/proveedores', methods=['GET'])(cnlistado_proveedores)
proveedor_bp.route('/proveedores', methods=['POST'])(cncrear_proveedor)
proveedor_bp.route('/proveedores/<string:id>', methods=['DELETE'])(cneliminar_proveedor)
proveedor_bp.route('/proveedores/<string:id>', methods=['PUT'])(cnactualizar_proveedor)