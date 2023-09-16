class Carta:
    def __init__(self,valor,palo):
        self.valor = valor
        self.palo = palo
        self.estado_boca_arriba = False

    def __str__(self):
        if self.estado_boca_arriba == True:
            return self.valor + self.palo
        else:
            return "-X"
    
    def __repr__(self):
        return str(self)