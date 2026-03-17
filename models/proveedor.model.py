class Proveedor:
    def __init__(self, id, nom, tel=None, dir=None,  corr=None):
        self.provId = id
        self.provNom = nom
        self.provTel = tel
        self.provCorr = corr
        self.provDir = dir

    def toDic(self):
        return {
            "provId": self.provId,
            "provNom": self.provNom,
            "provTel": self.provTel,
            "provCorr": self.provCorr,
            "provDir": self.provDir
        }