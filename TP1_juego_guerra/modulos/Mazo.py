import random
from Carta import Carta
from ListaDobleEnlazada import ListaDoblementeEnlazada

class Mazo:
    def __init__(self):
        self.mazo = ListaDoblementeEnlazada()
        self.valores = ['A','K','Q','J','10','9','8','7','6','5','4','3','2']
        self.palos = ['♠', '♥', '♦', '♣']
        self.crear_mazo()

    def crear_mazo(self):
        for valor in self.valores:
            for palo in self.palos:
                self.mazo.agregar_al_final(Carta(valor, palo))

    def poner_arriba(self, carta):
        self.mazo.agregar_al_inicio(carta)

    def sacar_arriba(self):
        return self.mazo.extraer(0)

    def poner_abajo(self, carta):
        self.mazo.agregar_al_final(carta)

    def mezclar(self):
        self.mazo.desordenar()
    
    def __str__(self):
        return str(self.mazo)