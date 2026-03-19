class usuario:
    def __init__(self, usuId, usuNom, usuApe, usuTel, usuCor, usuPassHash, usuRol, usuSupFK, usuEst, usuFecReg):
        self.usuId         = usuId
        self.usuNom        = usuNom
        self.usuApe        = usuApe
        self.usuTel        = usuTel
        self.usuCor        = usuCor
        self.usuPassHash   = usuPassHash
        self.usuRol        = usuRol
        self.usuSupFK      = usuSupFK
        self.usuEst        = usuEst
        self.usuFecReg     = usuFecReg
    # convertir objetos a diccionario
    def toDic(self):
        return {
            'usuId': self.usuId,
            'usuNom': self.usuNom,
            'usuApe': self.usuApe,
            'usuTel': self.usuTel,
            'usuCor': self.usuCor,
            'usuPassHash': self.usuPassHash,
            'usuRol': self.usuRol,
            'usuSupFK': self.usuSupFK,
            'usuEst': self.usuEst,
            'usuFecReg': self.usuFecReg
        }