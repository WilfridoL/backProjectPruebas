class pedidos:
    def __init__(
        self,
        pedId,
        pedCliIdFk,
        pedFecIng,
        pedFecEst,
        pedFecEnt,
        pedEstFk,
        pedObs,
        pedTolEst,
        pedTipPedFk,
        pedRecor,
        fotos=None,
        detalles=None
    ):
        self.pedId = pedId
        self.pedCliIdFk = pedCliIdFk
        self.pedFecIng = pedFecIng
        self.pedFecEst = pedFecEst
        self.pedFecEnt = pedFecEnt
        self.pedEstFk = pedEstFk
        self.pedObs = pedObs
        self.pedTolEst = pedTolEst
        self.pedTipPedFk = pedTipPedFk
        self.pedRecor = pedRecor

        self.detalles = detalles if detalles else []
        self.fotos = fotos if fotos else []

    def toDic(self):
        data = {
            'pedId': self.pedId,
            'pedCliIdFk': self.pedCliIdFk,
            'pedFecIng': self.pedFecIng,
            'pedFecEst': self.pedFecEst,
            'pedFecEnt': self.pedFecEnt,
            'pedEstFk': self.pedEstFk,
            'pedObs': self.pedObs,
            'pedTolEst': self.pedTolEst,
            'pedTipPedFk': self.pedTipPedFk,
            'pedRecor': self.pedRecor,
        }

        # Solo se agregan a data si traen datos
        if self.detalles:
            data["detalles"] = [d.toDic() for d in self.detalles]
        if self.fotos:
            data["fotos"] = [f.toDic() for f in self.fotos]

        return data