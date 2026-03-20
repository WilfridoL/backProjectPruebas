from flask import Blueprint
from controllers.productos_controller import cnlistado_productos

productos_bp = Blueprint('productos', __name__)
@productos_bp.route('/productos')
def listado_productos():
    return cnlistado_productos()