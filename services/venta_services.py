import re
from flask import current_app
from models.ventas_model import Ventas

def listado_ventas():
    c = current_app.mysql.connection.cursor()
    sql = "SELECT * FROM ventas"
    c.execute(sql)
    data = c.fetchall()
    
    d = []
    for p in data:
        obj = Ventas(
            venID=p[0],
            venFec=p[1],
            venDesc=p[2],
            estadoPago=p[3],
            venTotal=p[4],
            cliIdFk=p[5],
            usuIdFk=p[6],
            pedIdFk=p[7]
        ).toDic()
        d.append(obj)
    
    return d
def registrarVenta(
    id_cliente,
    id_usuario,
    fecha=None,
    descuento=0,
    estado_pago='SIN PAGAR',
    id_pedido=None,
    fecha_limite=None
):
    conn = current_app.mysql.connection
    c = conn.cursor()
    try:                                     
        c.execute("SELECT venID FROM ventas ORDER BY venID DESC LIMIT 1;")
        ultimo = c.fetchone()

        if ultimo and ultimo[0]:
            texto = str(ultimo[0])
            numero_texto = re.sub(r'[^0-9]', '', texto)
            if numero_texto:
                try:
                    num = int(numero_texto)
                except ValueError:
                    num = 0
                nuevo_num = num + 1
            else:
                nuevo_num = 1
        else:
            nuevo_num = 1

        venID = f"VT{str(nuevo_num).zfill(3)}"

        c.execute("SELECT 1 FROM usuario WHERE usuId = %s", (id_usuario,))
        if not c.fetchone():
            return {"error": "Usuario no existe"}

        c.execute("SELECT 1 FROM cliente WHERE cliId = %s", (id_cliente,))
        if not c.fetchone():
            return {"error": "Cliente no existe"}

        if id_pedido is not None:
            c.execute("SELECT 1 FROM pedidos WHERE pedId = %s", (id_pedido,))
            if not c.fetchone():
                return {"error": "Pedido no existe"}

        venta = Ventas(
            id=venID,
            fecha=fecha,
            desc=descuento,
            estPag=estado_pago,
            total=0.00,
            cliFk=id_cliente,
            usufk=id_usuario,
            pedFk=id_pedido
        )

        sql = """
        INSERT INTO ventas (
            venID, venFec, venDesc, estadoPago,
            venTotal, cliIdFk, usuIdFk, pedIdFk
        )
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
        """
        c.execute(sql, (
            venta.venId,
            venta.venFec,
            venta.venDesc,
            venta.estadoPago,
            venta.venTotal,
            venta.cliidFk,
            venta.usuFkID,
            venta.pedIdFk
        ))

        conn.commit()
        return {"message": "Venta registrada con éxito", "venta_id": venID}

    except Exception as e:                     
        conn.rollback()
        return {"error": str(e)}
    finally:                                    
        c.close()



def anularVenta(id):
    conn = current_app.mysql.connection
    c = conn.cursor()
    try:
        c.execute("SELECT estadoPago FROM ventas WHERE venID = %s;", (id,))
        venta = c.fetchone()

        if not venta:
            return {"error": f"Venta {id} no encontrada"}
        if venta[0] == 'ANULADO':
            return {"error": "La venta ya está anulada"}

       
        c.execute("""
            SELECT idProFk, cantidad 
            FROM det_venta WHERE idVenta = %s;
        """, (id,))
        detalles = c.fetchall()

        for detalle in detalles:
            c.execute("""
                UPDATE productos SET proStock = proStock + %s
                WHERE proId = %s;
            """, (detalle[1], detalle[0]))

        c.execute("""
            UPDATE ventas SET estadoPago = 'ANULADO'
            WHERE venID = %s;
        """, (id,))

        conn.commit()
        return {"message": f"Venta {id} anulada con éxito"}

    except Exception as e:
        conn.rollback()
        return {"error": str(e)}
    finally:
        c.close()
        
        