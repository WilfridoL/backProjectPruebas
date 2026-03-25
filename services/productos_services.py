from flask import current_app
from models.producto_model import Producto
def listado_productos():
    c=current_app.mysql.connection.cursor()
    sql="""
    SELECT proId, proNom, proStock, proPreUni, 
    proDesc, proGen, catNom, proTipPre, proTipPro, 
    proUmbMin, proTall, provNom, proEst FROM productos
    JOIN proveedor ON proProvFk = provId
    JOIN categoria ON catId = proCatFk
    """
    c.execute(sql)
    data=c.fetchall()
    # los datos se convierten a diccionari
    # x =[p for p in PendingDeprecationWarning]
    d = []
    for p in data:
        oblj=Producto(
            proId=p[0],
            proNom=p[1],
            proStock=p[2],
            proPreUni=p[3],
            proDesc=p[4],
            proGen=p[5],
            proCatFk=p[6],
            proTipPreFk=p[7],
            proTipPro=p[8],
            proUmbMin=p[9],
            proTallFk=p[10],
            proProv=p[11],
            proEst=p[12]
        ).toDic()
        d.append(oblj)
        
    return d


def buscarXid(id):
    return