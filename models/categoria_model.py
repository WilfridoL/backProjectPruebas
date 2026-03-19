class Categoria:
    def __init__(self, id, nom, desc=None):
        self.catId = id
        self.catNom = nom
        self.catDesc = desc

    def toDic(self):
        return {
            "catId": self.catId,
            "catNom": self.catNom,
            "catDesc": self.catDesc
        }