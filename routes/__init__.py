from .usuario_routes import usuarios_bp
from .cliente_routes import cliente_bp
from .pedidos_routes import pedidos_bp
from .productos import producto_bp
from .venta_routes import venta_bp
from .proveedores_routes import proveedor_bp
from .movimientos_routes import movimiento_bp

def cargarRutas(app):
    app.register_blueprint(producto_bp, url_prefix='/productos')
    app.register_blueprint(usuarios_bp, url_prefix='/usuarios')
    app.register_blueprint(cliente_bp, url_prefix='/clientes')
    app.register_blueprint(pedidos_bp, url_prefix='/pedidos')
    app.register_blueprint(venta_bp, url_prefix='/ventas')
    app.register_blueprint(proveedor_bp, url_prefix='/proveedores')
    app.register_blueprint(movimiento_bp, url_prefix='/movimientos')
    #app.register_blueprint(factura_blueprint ,url_prefix='/factura')

# __int__py
