class Det_venta:
    def __init__(self, id, idven, prodFk, cant, precio, sub):
        self.detVenId = id
        self.venId = idven
        self.idProFk = prodFk
        self.cantidad = cant
        self.precio = precio
        self.sub = sub

    def toDic(self):
        return {
            "detVenId": self.detVenId,
            "idVenta": self.venId,
            "idProFk": self.idProFk,
            "cantidad": self.cantidad,
            "precio": self.precio,
            "subtotal": self.sub
        }