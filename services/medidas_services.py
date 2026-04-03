from flask import current_app

def regMedidaPedido(
    id_pedido,
    id_medida,
    valor
):
  c = current_app.mysql.connection.cursor()
  sql = """
  INSERT INTO detPed_Med (detPedIdFK, detPedMedIdFk, detPedMedVal)
  VALUE (%s, %s, %s) 
  """
  c.execute(sql, (
      id_pedido,
      id_medida,
      valor
  ))
  current_app.mysql.connection.commit()
  c.close()
