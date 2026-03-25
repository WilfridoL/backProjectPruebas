from datetime import datetime

class Cliente:
    def __init__(self, cliId, cliNom, cliApe, cliTel, cliTel2, cliCorr, cliDir, usuFkID, cliEst, cliFecReg):
        self.cliId = cliId
        self.cliNom = cliNom
        self.cliApe = cliApe
        self.cliTel = cliTel
        self.cliTel2 = cliTel2
        self.cliCorr = cliCorr
        self.cliDir = cliDir
        self.usuFkID = usuFkID
        self.cliEst = cliEst
        self.cliFecReg = cliFecReg

    def toDic(self):
        return {
            "cliId": self.cliId,
            "cliNom": self.cliNom,
            "cliApe": self.cliApe,
            "cliTel": self.cliTel,
            "cliTel2": self.cliTel2,
            "cliCorr": self.cliCorr,
            "cliDir": self.cliDir,
            "usuFkID": self.usuFkID,
            "cliEst": self.cliEst,
            "cliFecReg": self.cliFecReg,
        }