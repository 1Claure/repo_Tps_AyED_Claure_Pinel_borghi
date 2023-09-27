
from Carta import Carta
from ListaDobleEnlazada import ListaDoblementeEnlazada

class Mazo:
    def __init__(self):
        self.mazo = ListaDoblementeEnlazada()
        self.valores = ['A','K','Q','J','10','9','8','7','6','5','4','3','2']
        self.palos = ['♠', '♥', '♦', '♣']

    def __repr__(self) -> str:
        return str(self.mazo)
    
    def __iter__(self):
        return iter(self.mazo)
    
    def __len__(self):
        return len(self.mazo)

    def crear_mazo(self):
        for valor in self.valores:
            for palo in self.palos:
                self.mazo.agregar_al_final(Carta(valor, palo))

    def poner_arriba(self, carta, boca_arriba = False):
        carta.estado_boca_arriba = boca_arriba
        self.mazo.agregar_al_inicio(carta)

    def sacar_arriba(self, boca_arriba = True):
        carta = self.mazo.extraer(0)
        carta.estado_boca_arriba = boca_arriba
        return carta 
    
    def sumar_cartas(self, cartas):
        return self.mazo.concatenar(cartas)

    def poner_abajo(self, carta, boca_arriba = False):
        carta.estado_boca_arriba = boca_arriba
        self.mazo.agregar_al_final(carta)

    def mezclar(self):
        self.mazo.desordenar()
    
    def __str__(self):
        return str(self.mazo)