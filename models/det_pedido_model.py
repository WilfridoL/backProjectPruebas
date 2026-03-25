class det_pedido:
    def __init__(self ,detPedId, pedObs, pedIdFk, cantidad, medidas=None, proIdFk = None):
        self.detPedId = detPedId
        self.pedObs = pedObs
        self.proIdFk = proIdFk
        self.pedIdFk = pedIdFk
        self.detPedCant = cantidad
        self.medidas = medidas if medidas else []

    def toDic(self):
        return {
            "detPedId": self.detPedId,
            "proIdFk": self.proIdFk,
            "detPedCant": self.detPedCant,
            "medidas": [m.toDic() for m in self.medidas]
        }