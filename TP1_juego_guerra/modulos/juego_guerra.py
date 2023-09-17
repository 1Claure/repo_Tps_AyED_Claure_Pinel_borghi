from Mazo import Mazo
import random

class Interfaz:
    def __init__(self, seed):
        
        self.jugador1 = Mazo()
        self.jugador2 = Mazo()
        self.cartas_en_mesa = Mazo()
        self.turno = 0
        self.estado_en_guerra = False
        self.cartas_boca_abajo = 3
        self.max_turnos = 9999
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
    
    def __iter__(self):
        return iter(self.cartas_en_mesa)

    def iniciar_juego(self):
        self.cartas_en_mesa.crear_mazo()
        self.cartas_en_mesa.mezclar()
        for _ in range(len(self.cartas_en_mesa) // 2):
            self.jugador1.poner_abajo(self.cartas_en_mesa.sacar_arriba())
            self.jugador2.poner_abajo(self.cartas_en_mesa.sacar_arriba())
        self.cartas_en_mesa = Mazo()

    def mostrar_turno(self):
        print(f"---------------------------------------\nTurno {self.turno}")
        print("Jugador 1:")
        jugador1_str = ' '.join(map(str, self.jugador1))  # Convierte la lista a una cadena
        jugador1_lineas = [jugador1_str[i:i+30] for i in range(0, len(jugador1_str), 30)]
        jugador1_formato = '\n'.join(jugador1_lineas)
        print(jugador1_formato)
        print("\n")
        print(self.cartas_en_mesa)
        print("\n")
        print("Jugador 2:")
        jugador2_str = ' '.join(map(str, self.jugador2))
        jugador2_lineas = [jugador2_str[i:i+30] for i in range(0, len(jugador2_str), 30)]
        jugador2_formato = '\n'.join(jugador2_lineas)
        print(jugador2_formato)
        print("\n")

    def jugar_turno(self):
        self.turno += 1

        carta_jugador1 = self.jugador1.sacar_arriba()
        carta_jugador2 = self.jugador2.sacar_arriba()

        puntaje_jugador1 = self.puntaje_carta[carta_jugador1.valor]
        puntaje_jugador2 = self.puntaje_carta[carta_jugador2.valor]

        self.cartas_en_mesa.poner_abajo(carta_jugador1, True)
        self.cartas_en_mesa.poner_abajo(carta_jugador2, True)

        self.mostrar_turno()

        if puntaje_jugador1 > puntaje_jugador2:
            print("¡Jugador 1 gana el turno!")
            for i in range(len(self.cartas_en_mesa)):
                carta = self.cartas_en_mesa.sacar_arriba()
                self.jugador1.poner_abajo(carta)
        elif puntaje_jugador1 < puntaje_jugador2:
            print("¡Jugador 2 gana el turno!")
            for i in range(len(self.cartas_en_mesa)):
                carta = self.cartas_en_mesa.sacar_arriba()
                self.jugador2.poner_abajo(carta)
        else:
            print("----------------¡Guerra!---------------")
            self.resolver_guerra()

    
    def resolver_guerra(self):
        # Comprueba que ambos jugadores tienen suficientes cartas para la guerra
        if len(self.jugador1) < self.cartas_boca_abajo + 1:
            print("El jugador 1 no tiene suficiente cartas para la guerra, el jugador 2 gana ¡Fin del juego!")
            return
        if len(self.jugador2) < self.cartas_boca_abajo + 1:
            print("El jugador 2 no tiene suficiente cartas para la guerra, el jugador 1 gana ¡Fin del juego!")
            return

        # Quita las cartas de los mazos de los jugadores
        for _ in range(self.cartas_boca_abajo):
            self.cartas_en_mesa.poner_abajo(self.jugador1.sacar_arriba())
            self.cartas_en_mesa.poner_abajo(self.jugador2.sacar_arriba())

    def mostrar_resultado(self):
        if self.turno > self.max_turnos:
            print("La partida ha alcanzado el máximo de turnos.")
            print("¡Empate!")
            return
        if len(self.jugador1) > len(self.jugador2):
            print("El jugador 2 no tiene suficiente cartas, el jugador 1 gana la partida ¡Fin del juego!")
        elif len(self.jugador1) < len(self.jugador2):
            print("¡El jugador 1 no tiene suficiente cartas, el jugador 2 gana la partida ¡Fin del juego!")
        else:
            print("¡Empate!")

seed = 42091269
juego = Interfaz(seed)
juego.iniciar_juego()
while juego.jugador1 and juego.jugador2 and juego.turno <= juego.max_turnos:
    juego.jugar_turno()

juego.mostrar_resultado()
