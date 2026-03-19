
from .productos import productos_bp
from .usuario_routes import usuarios_bp

def cargarRutas(app):
    app.register_blueprint(productos_bp, url_prefix='/producto')
    app.register_blueprint(usuarios_bp, url_prefix='/usuario')
    #app.register_blueprint(factura_blueprint ,url_prefix='/factura')

# __int__py
