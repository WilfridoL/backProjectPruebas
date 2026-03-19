from datetime import datetime

class Ventas:
    def __init__(self, id, desc, estPag, total, cliFk, usufk,pedFk=None):
        self.venId = id
        self.venFac = datetime.now().strftime("%d/%m/%Y")
        self.venDesc = desc
        self.estadoPago = estPag
        self.venTotal = total
        self.cliidFk = cliFk
        self.usuFkID = usufk
        self.pedIdFk = pedFk

    def toDic(self):
        return {
            "venId": self.venid,
            "venDesc": self.venDesc,
            "estadoPago": self.estadoPago,
            "venTotal": self.venTotal,
            "cliidFk": self.cliidFk,
            "usuFkID": self.usuFkID,
            "pedIdFk": self.pedIdFk
        }