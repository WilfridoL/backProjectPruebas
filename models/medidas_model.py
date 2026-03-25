class Medidas:
    def __init__(self, medId, medNom, medVal=None, medDesc=None):
        self.medId = medId
        self.medNom = medNom
        self.medDesc = medDesc
        self.medVal = medVal

    def toDic(self):
        return {
            "medId": self.medId,
            "medNom": self.medNom,
            "medDesc": self.medDesc,
            "medVal": self.medVal
        }