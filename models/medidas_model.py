class Medidas:
    def __init__(self, medId, medNom, medVal=None, medDesc=None):
        self.medId = medId
        self.medNom = medNom
        self.medDesc = medDesc
        self.medVal = medVal

    def toDic(self):
        return self.clean_dict({
            "medId": self.medId,
            "medNom": self.medNom,
            "medDesc": self.medDesc,
            "medVal": self.medVal
        })
    def clean_dict(self, data):
         return {k: v for k, v in data.items() if v is not None}