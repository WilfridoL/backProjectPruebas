from .usuario_routes import usuarios_bp
from .cliente_routes import cliente_bp
from .pedidos_routes import pedidos_bp
from .productos import producto_bp

def cargarRutas(app):
    app.register_blueprint(producto_bp, url_prefix='/productos')
    app.register_blueprint(usuarios_bp, url_prefix='/usuario')
    app.register_blueprint(cliente_bp, url_prefix='/cliente')
    app.register_blueprint(pedidos_bp, url_prefix='/pedidos')
    #app.register_blueprint(factura_blueprint ,url_prefix='/factura')

# __int__py
