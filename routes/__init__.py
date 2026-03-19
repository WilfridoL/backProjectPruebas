
from .productos import productos_bp
from .usuario_routes import usaurios_bp

def cargarRutas(app):
    app.register_blueprint(productos_bp ,url_prefix='/producto')
    app.register_blueprint(usaurios_bp, url_prefix='/usaurio')
    #app.register_blueprint(factura_blueprint ,url_prefix='/factura')

# __int__py
