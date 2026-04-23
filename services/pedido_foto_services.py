from flask import current_app, jsonify

def registrarFoto(
    id_pedido,
    url
):
  conect = current_app.mysql.connection
  c = conect.cursor()
  try:

    sql_foto = """
    INSERT INTO pedido_foto (pedIdFk, fotUrl)
    VALUES (%s, %s)
    """

    c.execute(sql_foto, (id_pedido, url,))

    conect.commit()

    return jsonify({
      "message": "se añadio una nueva foto al pedido",
      "url": url,
    }), 201
  
  except  Exception as e:
    conect.rollback()
    return jsonify({"error": str(e)}), 500
  finally:
    c.close()

def eliminarFoto(id_foto, id_pedido):
    conect = current_app.mysql.connection
    c = conect.cursor()
    try:
        sql = "DELETE FROM pedido_foto WHERE fotId = %s AND pedIdFk = %s"

        c.execute(sql, (id_foto, id_pedido))
        conect.commit()

        if c.rowcount == 0:
            return jsonify({
                "error": "Foto no encontrada"
            }), 404

        return jsonify({
            "message": "Foto eliminada correctamente"
        }), 200

    except Exception as e:
        conect.rollback()
        return jsonify({"error": str(e)}), 500

    finally:
        c.close()