from datetime import datetime

class Ventas:
    def __init__(self, id, fecha=None, desc=0, estPag='SIN PAGAR', total=0.00, cliFk=None, usufk=None, pedFk=None):
        self.venId = id
        self.venFec = fecha or datetime.now().strftime("%Y-%m-%d")
        self.venDesc = desc
        self.estadoPago = estPag
        self.venTotal = total
        self.cliidFk = cliFk
        self.usuFkID = usufk
        self.pedIdFk = pedFk

    def toDic(self):
        return {
            "venId": self.venId,
            "venFec": self.venFec,
            "venDesc": self.venDesc,
            "estadoPago": self.estadoPago,
            "venTotal": self.venTotal,
            "cliidFk": self.cliidFk,
            "usuFkID": self.usuFkID,
            "pedIdFk": self.pedIdFk
        }
    