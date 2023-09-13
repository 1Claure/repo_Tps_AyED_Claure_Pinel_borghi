from Mazo import Mazo
import random

class Juego:
    def __init__(self, seed):
        self.mazo = Mazo()
        self.jugador1 = []
        self.jugador2 = []
        self.turno = 1
        self.max_turnos = 10
        self.puntaje_carta = {
            "2": 2,
            "3": 3,
            "4": 4,
            "5": 5,
            "6": 6,
            "7": 7,
            "8": 8,
            "9": 9,
            "10": 10,
            "J": 11,
            "Q": 12,
            "K": 13,
            "A": 14
        }
        random.seed(seed)  #Uso una semilla de generación aleatoria para probar distintos escenarios

    def iniciar_juego(self):
        self.mazo.mezclar()
        for _ in range(26):
            self.jugador1.append(self.mazo.sacar_arriba())
            self.jugador2.append(self.mazo.sacar_arriba())

    def jugar_turno(self):
        if self.turno > self.max_turnos:
            print("La partida ha alcanzado el máximo de turnos.")
            print("¡Empate!")
            return

        print(f"--------------\nTurno {self.turno}")
        print("Jugador 1:")
        print("-" + " -".join(str(carta) for carta in self.jugador1))
        print("Jugador 2:")
        print("-" + " -".join(str(carta) for carta in self.jugador2))

        carta_jugador1 = self.jugador1.pop(0)
        carta_jugador2 = self.jugador2.pop(0)
        print(f"\n{carta_jugador1} {carta_jugador2}")

        puntaje_jugador1 = self.puntaje_carta[carta_jugador1.valor]
        puntaje_jugador2 = self.puntaje_carta[carta_jugador2.valor]

        if puntaje_jugador1 > puntaje_jugador2:
            print("¡Jugador 1 gana el turno!")
            self.jugador1.append(carta_jugador1)
            self.jugador1.append(carta_jugador2)
        elif puntaje_jugador1 < puntaje_jugador2:
            print("¡Jugador 2 gana el turno!")
            self.jugador2.append(carta_jugador1)
            self.jugador2.append(carta_jugador2)
        else:
            print("Empate")

        self.turno += 1

    def mostrar_resultado(self):
        if len(self.jugador1) > len(self.jugador2):
            print("¡Jugador 1 gana la partida!")
        elif len(self.jugador1) < len(self.jugador2):
            print("¡Jugador 2 gana la partida!")
        else:
            print("¡Empate!")

seed = 1231
juego = Juego(seed)
juego.iniciar_juego()
while juego.jugador1 and juego.jugador2 and juego.turno <= juego.max_turnos:
    juego.jugar_turno()

juego.mostrar_resultado()
        
