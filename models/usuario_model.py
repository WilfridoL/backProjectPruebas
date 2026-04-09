class Usuario:   # ← Capital U
    def __init__(self, usuId, usuNom, usuApe, usuTel, usuCor, usuPassHash, usuRol, usuSupFk, usuEst, usuFecReg):
        self.usuId       = usuId
        self.usuNom      = usuNom
        self.usuApe      = usuApe
        self.usuTel      = usuTel
        self.usuCor      = usuCor
        self.usuPassHash = usuPassHash
        self.usuRol      = usuRol
        self.usuSupFk    = usuSupFk   # ← k minúscula
        self.usuEst      = usuEst
        self.usuFecReg   = usuFecReg

    def toDic(self):
        return {
            'usuId':       self.usuId,
            'usuNom':      self.usuNom,
            'usuApe':      self.usuApe,
            'usuTel':      self.usuTel,
            'usuCor':      self.usuCor,
            'usuPassHash': self.usuPassHash,
            'usuRol':      self.usuRol,
            'usuSupFk':    self.usuSupFk,   # ← k minúscula
            'usuEst':      self.usuEst,
            'usuFecReg':   self.usuFecReg
        }