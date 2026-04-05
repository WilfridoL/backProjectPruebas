from flask import current_app
from models.pedidos_model import pedidos
from models.det_pedido_model import det_pedido
from models.medidas_model import Medidas
from models.pedido_foto_model import Foto_Pedido

def listarPedidos():
    c = current_app.mysql.connection.cursor()

    c.execute("SELECT * FROM pedidos")
    pedidos_db = c.fetchall()

    resultado = []

    for p in pedidos_db:
        pedId = p[0]
        listar_fotos = []

        c.execute("""
            SELECT fotId, fotUrl, fotFec FROM pedido_foto
            WHERE pedIdFk = %s
        """, (pedId,))
        foto_db = c.fetchall()
        for f in foto_db:
            listar_fotos.append(
                Foto_Pedido(
                    fotId=f[0],
                    fotUrl=f[1],
                    fotFec=f[2]
                )
            )


        c.execute("""
            SELECT detPedId, pedObs, proIdFk, pedIdFk, detPedCant
            FROM det_pedido
            WHERE pedIdFk = %s
        """, (pedId,))
        detalles_db = c.fetchall()

        lista_detalles = []

        for d in detalles_db:
            detPedId = d[0]
            print(d[1])
            
            c.execute("""
                SELECT m.medId, m.medNom, dm.detPedMedVal
                FROM detPed_Med dm
                JOIN medidas m ON m.medId = dm.detPedMedIdFk
                WHERE dm.detPedIdFk = %s
            """, (detPedId,))
            medidas_db = c.fetchall()

            lista_medidas = [
                Medidas(m[0], m[1], m[2]) for m in medidas_db
            ]

            lista_detalles.append(
                det_pedido(
                    detPedId=d[0],
                    pedObs=d[1],
                    proIdFk=d[2],
                    pedIdFk=d[3],
                    cantidad=d[4],
                    medidas=lista_medidas
                )
            )

        pedido_obj = pedidos(
           pedId=p[0],
            pedCliIdFk=p[1],
            pedFecIng=p[2],
            pedFecEst=p[3],
            pedFecEnt=p[4],
            pedEstFk=p[5],
            pedObs=p[6],
            pedTolEst=p[7],
            pedTipPedFk=p[8],
            pedRecor=p[9],
            detalles=lista_detalles,
            fotos= listar_fotos
        ).toDic()

        resultado.append(pedido_obj)

    return resultado


def regPedidos(
        id,
        id_cliente,
        tipo_pedido,
        fecha_estimada = None,
        dias_recordatorio = None,
        precio_total_estimado = None,
        observacion = None
):

    c = current_app.mysql.connection.cursor()
    sql = """
    INSERT INTO pedidos (pedId, pedCliIdFk, pedFecIng, pedFecEst, pedObs, pedTolEst, pedTipPed, pedRecor)
    VALUE (%s, %s, NOW(), %s, %s, %s, %s, %s) 
    """

    c.execute(sql, (
        id,
        id_cliente,
        fecha_estimada,
        observacion,
        precio_total_estimado,
        tipo_pedido,
        dias_recordatorio
    ))
    current_app.mysql.connection.commit()
    c.close()

def delPedido(id):
    conect = current_app.mysql.connection
    c = conect.cursor()
    try:
        # cambia el estado del pedido a cancelado
        sql_pedido = """
        UPDATE pedidos SET
        pedEst = 'CANCELADO'
        WHERE pedId = %s
        """
        
        c.execute(sql_pedido, (id,))

        conect.commit()

        return {
            "message": "Se cancelo el pedido con exito"
        }
    except Exception as e:
        conect.rollback()
        return {"error": str(e)}
    finally:
        c.close()
    