class Mazo:
    def __init__(self):
        self.cartas = []
        self.valores = ['A','K','Q','J','10','9','8','7','6','5','4','3','2']
        self.palos = ['♠', '♥', '♦', '♣']
        self.crear_mazo()
        self.agregar_carta()
        self.quitar_carta()

    def crear_mazo(self):
        for i in range(self.valores):
            for j in range(self.palos):
                self.cartas.append(Carta(self.valores[i] + self.palos[j]))
    
    def agregar_carta(self, carta):
        self.cartas.append(carta)

    def quitar_carta(self, carta): #pone la carta del mazo en la mesa
        self.cartas(carta)


class Carta:
    def __init__(self,valor,palo):
        self.valor = valor
        self.palo = palo
