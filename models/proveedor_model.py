class Proveedor:
    def __init__(self, provId, provNom, provTel=None, provCorr=None, provDir=None):
        self.provId  = provId
        self.provNom = provNom
        self.provTel = provTel
        self.provCorr = provCorr
        self.provDir = provDir

    def toDic(self):
        return {
            "provId":  self.provId,
            "provNom": self.provNom,
            "provTel": self.provTel,
            "provCorr": self.provCorr,
            "provDir": self.provDir
        }