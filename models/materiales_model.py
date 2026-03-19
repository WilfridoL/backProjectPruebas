class materiales:
    def __init__(self,matId,matNom,matEst,matDesc,matUmbMin,matCantDisp,matUniMed,matPreUni,matProv,matTipMat):
        self.matId = matId
        self.matNom = matNom
        self.matEst = matEst
        self.matDesc = matDesc
        self.matUmbMin = matUmbMin
        self.matCantDisp = matCantDisp
        self.matUniMed = matUniMed
        self.matPreUni = matPreUni
        self.matProv = matProv
        self.matTipMat = matTipMat  
    def toDic(self):
        return {
            'matId': self.matId,
            'matNom': self.matNom,
            'matEst': self.matEst,
            'matDesc': self.matDesc,
            'matUmbMin': self.matUmbMin,
            'matCantDisp': self.matCantDisp,
            'matUniMed': self.matUniMed,
            'matPreUni': self.matPreUni,
            'matProv': self.matProv,
            'matTipMat': self.matTipMat
        }