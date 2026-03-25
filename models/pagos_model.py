from datetime import datetime

class Det_venta:
    def __init__(self, id, idven, monto, pagFec,  est):
        self.pagId = id
        self.pagVenId = idven
        self.pagMon = monto
        self.pagFec = pagFec
        self.pagEst = est

    def toDic(self):
        return {
            "pagId": self.pagId,
            "pagVenId": self.pagVenId,
            "pagMon": self.pagMon,
            "pagFec": self.pagFec,
            "pagEst": self.pagEst
        }