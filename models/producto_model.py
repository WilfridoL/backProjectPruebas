class Producto:
    def __init__(self, 
    proId, 
    proNom, 
    proStock, 
    proPreUni, 
    proEst,
    proDesc=None, 
    proGen=None, 
    proCatFk=None,
    proTipPreFk=None, 
    proTipPro=None,
    proUmbMin=None, 
    proTallFk=None, 
    proProv=None):

        self.proId = proId
        self.proNom = proNom
        self.proStock = proStock
        self.proPreUni = proPreUni
        self.proDesc = proDesc
        self.proGen = proGen
        self.proCatFk = proCatFk
        self.proTipPreFk = proTipPreFk
        self.proTipPro = proTipPro
        self.proUmbMin = proUmbMin
        self.proTallFk = proTallFk
        self.proProv = proProv,
        self.proEst = proEst

    def toDic(self):
        return {
            "proId": self.proId,
            "proNom": self.proNom,
            "proStock": self.proStock,
            "proPreUni": self.proPreUni,
            "proDesc": self.proDesc,
            "proGen": self.proGen,
            "proCatFk": self.proCatFk,
            "proTipPreFk": self.proTipPreFk,
            "proTipPro": self.proTipPro,
            "proUmbMin": self.proUmbMin,
            "proTallFk": self.proTallFk,
            "proProv": self.proProv,
            "proEst": self.proEst
        }