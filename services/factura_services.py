import re
from datetime import datetime
from flask import current_app
from models.factura_model import Factura

def listado_factura():
    c=current_app.mysql.connection.cursor()
    sql="SELECT * FROM factura"
    c.execute(sql)
    data=c.fetchall()
    # los datos se convierten a diccionario
    return data
def buscarXid(id):
    c=current_app.mysql.connection.cursor()
    sql="SELECT * FROM factura WHERE facId=%s"
    c.execute(sql, (id,))
    data=c.fetchone()
    return data
def crear_factura(facId, facTotal, numfatura, facFecEmi=None):
    conn = current_app.mysql.connection
    c = conn.cursor()
    try:
        c.execute("SELECT 1 FROM ventas WHERE venID = %s", (facId,))
        if not c.fetchone():
            return {"error": "Venta no existe para esa factura"}

        c.execute("SELECT facId FROM factura WHERE facId = %s", (facId,))
        if c.fetchone():
            return {"error": "Factura ya existe para esa venta"}

        if not facFecEmi:
            facFecEmi = datetime.now().strftime("%Y-%m-%d")

        sql = """
        INSERT INTO factura (facId, facFecEmi, facTotal, numfatura)
        VALUES (%s, %s, %s, %s)
        """
        c.execute(sql, (facId, facFecEmi, facTotal, numfatura))
        conn.commit()
        return {"message": "Factura creada con éxito", "facId": facId}

    except Exception as e:
        conn.rollback()
        return {"error": str(e)}

    finally:
        c.close()


def eliminar_factura(id):
    conn = current_app.mysql.connection
    c = conn.cursor()
    try:
        c.execute("SELECT facId FROM factura WHERE facId = %s", (id,))
        if not c.fetchone():
            return {"error": "Factura no encontrada"}

        c.execute("DELETE FROM factura WHERE facId = %s", (id,))
        conn.commit()
        return {"message": "Factura eliminada con éxito"}

    except Exception as e:
        conn.rollback()
        return {"error": str(e)}

    finally:
        c.close()