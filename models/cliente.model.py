from datetime import datetime

class Cliente:
    def __init__(self, id, nom, ape, tel, tel2, corr, dir, usufk, est):
        self.cliId = id
        self.nom = nom
        self.cliApe = ape
        self.cliTel = tel
        self.cliTel2 = tel2
        self.cliCorr = corr
        self.cliDir = dir
        self.usuFkID = usufk
        self.cliEst = est
        self.cliFecReg = datetime.now().strftime("%d/%m/%Y")

    def toDic(self):
        return {
            "cliId": self.cliId,
            "nom": self.nom,
            "cliApe": self.cliApe,
            "cliTel": self.cliTel,
            "cliTel2": self.cliTel2,
            "cliCorr": self.cliCorr,
            "cliDir": self.cliDir,
            "usuFkID": self.usuFkID,
            "cliEst": self.cliEst,
            "cliFecReg": self.cliFecReg
        }