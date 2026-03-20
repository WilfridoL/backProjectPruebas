
from .producto import producto_blueprint

def cargarRutas(app):
    app.register_blueprint(producto_blueprint ,url_prefix='/producto')
    #app.register_blueprint(factura_blueprint ,url_prefix='/factura')

