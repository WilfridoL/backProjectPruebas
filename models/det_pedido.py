class det_pedido:
    def __init__(self ,detPedId,detMedPec,detMedCad,detMedCin,detMedLarMan,detMedAncEsp,detMedConMus,detMedLarPan,pedObs,codigoFk,pedIdFk):
        self.detPedId = detPedId
        self.detMedPec = detMedPec
        self.detMedCad = detMedCad
        self.detMedCin = detMedCin
        self.detMedLarMan = detMedLarMan
        self.detMedAncEsp = detMedAncEsp
        self.detMedConMus = detMedConMus
        self.detMedLarPan = detMedLarPan
        self.pedObs = pedObs
        self.codigoFk = codigoFk
        self.pedIdFk = pedIdFk
    def toDic(self):        return {
            'detPedId': self.detPedId,
            'detMedPec': self.detMedPec,
            'detMedCad': self.detMedCad,
            'detMedCin': self.detMedCin,
            'detMedLarMan': self.detMedLarMan,
            'detMedAncEsp': self.detMedAncEsp,
            'detMedConMus': self.detMedConMus,
            'detMedLarPan': self.detMedLarPan,
            'pedObs': self.pedObs,
            'codigoFk': self.codigoFk,
            'pedIdFk': self.pedIdFk
        }   
