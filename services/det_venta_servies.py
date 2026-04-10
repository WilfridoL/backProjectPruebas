import re
from flask import current_app
from models.det_venta_model import Det_venta

def listado_det_venta():
    c = current_app.mysql.connection.cursor()
    sql = "SELECT * FROM det_venta"
    c.execute(sql)
    data = c.fetchall()
    
    d = []
    for p in data:
        obj = Det_venta(
            detVenId=p[0],
            idVenta=p[1],
            idProFk=p[2],
            cantidad=p[3],
            precio=p[4],
            subtotal=p[5]
        ).toDic()
        d.append(obj)
    
    return d


def registrarDetalleVenta(id_venta, id_producto, cantidad, precio):
    conn = current_app.mysql.connection
    c = conn.cursor()
    try:
        c.execute("SELECT 1 FROM ventas WHERE venID = %s", (id_venta,))
        if not c.fetchone():
            return {"error": f"Venta {id_venta} no encontrada"}

        c.execute("""
            SELECT proStock FROM productos
            WHERE proId = %s AND proEst = 1;
        """, (id_producto,))
        producto = c.fetchone()

        if not producto:
            return {"error": f"Producto {id_producto} no encontrado o inactivo"}
        if producto[0] < cantidad:
            return {"error": f"Stock insuficiente. Disponible: {producto[0]}, solicitado: {cantidad}"}

        c.execute("SELECT detVenId FROM det_venta ORDER BY detVenId DESC LIMIT 1")
        ultimo = c.fetchone()
        if ultimo and ultimo[0]:
            texto = str(ultimo[0])
            numero_texto = re.sub(r'[^0-9]', '', texto)
            num = int(numero_texto) if numero_texto else 0
            nuevo_num = num + 1
        else:
            nuevo_num = 1

        detVenId = f"DV{str(nuevo_num).zfill(3)}"

        # Calcular subtotal y crear objeto modelo
        subtotal = round(precio * cantidad, 2)
        detalle = Det_venta(
            id=detVenId,
            idven=id_venta,
            prodFk=id_producto,
            cant=cantidad,
            precio=precio,
            sub=subtotal
        )

        # Insertar detalle
        sql = """
        INSERT INTO det_venta (
            detVenId, idVenta, idProFk,
            cantidad, precio, subtotal
        )
        VALUES (%s, %s, %s, %s, %s, %s)
        """
        c.execute(sql, (
            detalle.detVenId,
            detalle.venId,
            detalle.idProFk,
            detalle.cantidad,
            detalle.precio,
            detalle.sub
        ))

        # Descontar stock
        c.execute("""
            UPDATE productos SET proStock = proStock - %s
            WHERE proId = %s;
        """, (cantidad, id_producto))

        # Recalcular venTotal en la venta
        c.execute("""
            UPDATE ventas SET
                venTotal = (
                    SELECT SUM(subtotal)
                    FROM det_venta
                    WHERE idVenta = %s
                )
            WHERE venID = %s;
        """, (id_venta, id_venta))

        conn.commit()
        return {"message": "Detalle registrado con éxito", "data": detalle.toDic()}

    except Exception as e:
        conn.rollback()
        return {"error": str(e)}
    finally:
        c.close()


def eliminarDetalleVenta(id):
    conn = current_app.mysql.connection
    c = conn.cursor()
    try:
        # Obtener datos del detalle antes de eliminar
        c.execute("""
            SELECT idProFk, cantidad, idVenta
            FROM det_venta WHERE detVenId = %s;
        """, (id,))
        detalle = c.fetchone()

        if not detalle:
            return {"error": "Detalle no encontrado"}

        id_producto = detalle[0]
        cantidad    = detalle[1]
        id_venta    = detalle[2]

        # Devolver stock al producto
        c.execute("""
            UPDATE productos SET proStock = proStock + %s
            WHERE proId = %s;
        """, (cantidad, id_producto))

        # Eliminar detalle
        c.execute("DELETE FROM det_venta WHERE detVenId = %s;", (id,))

        # Recalcular venTotal (COALESCE por si era el ultimo detalle)
        c.execute("""
            UPDATE ventas SET
                venTotal = COALESCE((
                    SELECT SUM(subtotal)
                    FROM det_venta
                    WHERE idVenta = %s
                ), 0.00)
            WHERE venID = %s;
        """, (id_venta, id_venta))

        conn.commit()
        return {"message": "Detalle eliminado con éxito"}

    except Exception as e:
        conn.rollback()
        return {"error": str(e)}
    finally:
        c.close()