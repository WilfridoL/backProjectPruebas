class Producto:
    def __init__(self, id, nom, stock, preUni, desc=None, gen=None, catFk=None,
                 tipPreFk=None, tipPro=None, proUmbMin=None, tall=None, pro=None):

        self.proId = id
        self.proNom = nom
        self.proStock = stock
        self.proPreUni = preUni
        self.proDesc = desc
        self.proGen = gen
        self.proCatFk = catFk
        self.proTipPreFk = tipPreFk
        self.proTipPro = tipPro
        self.proUmbMin = proUmbMin
        self.proTallFk = tall
        self.proProv = pro

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
            "proProv": self.proProv
        }