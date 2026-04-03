from flask import current_app
from services.medidas_services import regMedidaPedido

def regDetallePedido(
    id,              # id del detalle
    id_pedido,
    cantidad,
    precio,
    nombre,
    tipo_prenda=None,
    talla=None,
    observacion=None,
    medidas=None
):
    conn = current_app.mysql.connection
    c = conn.cursor()

    try:
        # 🔥 1. Generar ID tipo PR002
        c.execute("SELECT proId FROM productos ORDER BY proId DESC LIMIT 1;")
        ultimo = c.fetchone()
        if ultimo:
            num = int(ultimo[0].replace("PR", ""))
            nuevo_num = num + 1
        else:
            nuevo_num = 1
        proId = f"PR{str(nuevo_num).zfill(3)}"
        # 🔥 2. Insertar producto
        sql_producto = """
        INSERT INTO productos (
            proId, proNom, proStock, proPreUni, 
            proTipPre, proTall, proTipPro, proEst
        )
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
        """

        c.execute(sql_producto, (
            proId,
            nombre,
            0,                  # stock inicial
            precio,
            tipo_prenda,
            talla,
            'PERSONALIZADO',
            3                   # estado por defecto
        ))

        # 🔥 3. Insertar detalle del pedido
        sql_detalle = """
        INSERT INTO det_pedido (
            detPedId, pedIdFk, proIdFk, 
            detPedCant, pedObs
        )
        VALUES (%s, %s, %s, %s, %s)
        """

        c.execute(sql_detalle, (
            id,
            id_pedido,
            proId,
            cantidad,
            observacion
        ))

        if medidas and isinstance(medidas, list):
             for medida in medidas:

              # Validar que sea objeto
              if not isinstance(medida, dict):
                  continue

              # Extraer datos
              id_medida = medida.get("id_medida")
              valor = medida.get("valor")

              # Validar que vengan los campos necesarios
              if id_medida is None or valor is None:
                  continue

              # Llamar función
              regMedidaPedido(id, id_medida, valor)

        conn.commit()

        return {
            "message": "Detalle de pedido registrado",
            "producto_id": proId
        }

    except Exception as e:
        conn.rollback()
        return {"error": str(e)}

    finally:
        c.close()