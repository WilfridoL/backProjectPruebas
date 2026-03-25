class Foto_Pedido:
    def __init__(self, fotId, fotUrl, fotFec):
        self.fotId = fotId
        self.fotUrl = fotUrl
        self.fotFec = fotFec

    def toDic(self):
        return {
            "fotId": self.fotId,
            "fotUrl": self.fotUrl,
            "fotFec": self.fotFec,
        }