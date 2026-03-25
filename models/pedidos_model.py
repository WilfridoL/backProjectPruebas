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

        # ✅ listas correctas
        self.detalles = detalles if detalles else []
        self.fotos = fotos if fotos else []

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
            'pedTipPedFk': self.pedTipPedFk,
            'pedRecor': self.pedRecor,

            # 🔽 relaciones al final (más limpio)
            "detalles": [d.toDic() for d in self.detalles],
            "fotos": [f.toDic() for f in self.fotos]
        }