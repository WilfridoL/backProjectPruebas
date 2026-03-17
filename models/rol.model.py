class Rol:
    def __init__(self, id, nom, desc=None):
        self.rolId = id
        self.rolNom = nom
        self.rolDesc = desc

    def toDic(self):
        return {
            "rolId": self.rolId,
            "rolNom": self.rolNom,
            "rolDesc": self.rolDesc
        }