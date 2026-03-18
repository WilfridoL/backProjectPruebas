class factura:
    def __init__(self,facId,facFecEmi,facTotal,numfactura):
        self.facId = facId
        self.facFecEmi = facFecEmi
        self.facTotal = facTotal
        self.numfactura = numfactura
    def toDic(self):        return {
            'facId': self.facId,
            'facFecEmi': self.facFecEmi,
            'facTotal': self.facTotal,
            'numfactura': self.numfactura
        }
    