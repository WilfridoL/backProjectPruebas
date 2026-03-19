class pedidos:
    def __init__(self,pedId,pedCliIdFk,pedFecIng,pedFecEst,pedFecEnt,pedEstFk,pedObs,pedTolEst,pedTipPedFk):
        self.pedId = pedId
        self.pedCliIdFk = pedCliIdFk
        self.pedFecIng = pedFecIng
        self.pedFecEst = pedFecEst
        self.pedFecEnt = pedFecEnt
        self.pedEstFk = pedEstFk
        self.pedObs = pedObs
        self.pedTolEst = pedTolEst
        self.pedTipPedFk = pedTipPedFk
    def toDic(self):
        return {
            'pedId': self.pedId,
            'pedCliIdFk': self.pedCliIdFk,
            'pedFecIng': self.pedFecIng,
            'pedFecEst': self.pedFecEst,
            'pedFecEnt': self.pedFecEnt,
            'pedEstFk': self.pedEstFk,
            'pedObs': self.pedObs,
            'pedTolEst': self.pedTolEst,
            'pedTipPedFk': self.pedTipPedFk
        }