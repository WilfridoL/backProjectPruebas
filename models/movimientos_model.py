class movimientos:
    def __init__(self, idMov, tipo, cantidad, fecha, observacion, usuIdFK):
        self.idMov         = idMov
        self.tipo          = tipo
        self.cantidad      = cantidad
        self.fecha         = fecha
        self.observacion   = observacion
        self.usuIdFK       = usuIdFK
    def toDic(self):
        return {
            'idMov': self.idMov,
            'tipo': self.tipo,
            'cantidad': self.cantidad,
            'fecha': self.fecha,
            'observacion': self.observacion,
            'usuIdFK': self.usuIdFK
        }