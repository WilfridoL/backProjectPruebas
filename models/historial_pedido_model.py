class historial_pedido:
    def __init__(self, histId, pedIdFk, estadoAnterior, estadoNuevo, usuIdFk, hisFec):
        self.histId = histId
        self.pedIdFk = pedIdFk
        self.estadoAnterior = estadoAnterior
        self.estadoNuevo = estadoNuevo
        self.usuIdFk = usuIdFk
        self.hisFec = hisFec
    def toDic(self):        return {
            'histId': self.histId,
            'pedIdFk': self.pedIdFk,
            'estadoAnterior': self.estadoAnterior,
            'estadoNuevo': self.estadoNuevo,
            'usuIdFk': self.usuIdFk,
            'hisFec': self.hisFec
        }
    