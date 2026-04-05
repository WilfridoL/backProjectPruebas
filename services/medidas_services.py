from flask import current_app, jsonify
# registra una o varias medidas al detalle asociado
def regMedidaPedido(
    id_pedido,
    id_medida,
    valor
):
    conect = current_app.mysql.connection
    c = conect.cursor()

    try:
        # validar que exista el id de la medida
        sql_medida = """
				SELECT * FROM medidas WHERE medId = %s
				"""
        c.execute(sql_medida, (id_medida,))
        
        if c.rowcount == 0: return jsonify({"error": "No existe una medida registrada con el id proporcionado."}), 404
        
		# validar duplicados
        c.execute("""
            SELECT * FROM detPed_Med
            WHERE detPedIdFK = %s AND
            detPedMedIdFk = %s
        """, (id_pedido, id_medida,))

        if c.rowcount > 0: return jsonify({"error": "El registro ya existe. No se permiten duplicados."}), 409

		# registrar la nueva medida al detalle
        sql_dpMed = """
            INSERT INTO detPed_Med (detPedIdFK, detPedMedIdFk, detPedMedVal)
            VALUE (%s, %s, %s) 
        """
        c.execute(sql_dpMed, (
            id_pedido,
            id_medida,
            valor
        ))
        
        conect.commit()

        return jsonify({
            "message": f"se registro con exito una nueva medida al detalle de pedido de codigo {id_pedido}"
				}), 201
    except Exception as e:
        conect.rollback()
        return jsonify({"error": str(e)}), 500 
    finally:
        c.close()

# elimina una medida especifica asociada al detalle
def eliminarMedidaEspecifica(id_detalle, id_medida):
    conexion = current_app.mysql.connection
    c = conexion.cursor()

    try:
        c.execute("""
            DELETE FROM detPed_Med
            WHERE detPedIdFk = %s AND detPedMedIdFk = %s
        """, (id_detalle, id_medida))

        if c.rowcount == 0:
            return {"error": "No se encontró la medida asociada al detalle."}, 404

        conexion.commit()
        return {"message": "Medida eliminada correctamente."}, 200

    except Exception as e:
        conexion.rollback()
        return {"error": str(e)}, 500

    finally:
        c.close()

# elimina todas las medidas de detalle
def eliminarMedidas(id):
    c = current_app.mysql.connection.cursor()
    c.execute("""
    DELETE FROM detPed_Med
    WHERE  detPedIdFk = %s
    """, (id,))
    current_app.mysql.connection.commit()
    c.close()

