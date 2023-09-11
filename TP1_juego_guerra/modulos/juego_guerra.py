import random

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
    
   # def agregar_carta(self, carta):
   # self.cartas.append(carta)

    def poner_arriba(self, carta):
        nodo = Nodo(carta)
        if self.mazo is None:
            self.mazo = nodo
        else:
            nodo.siguiente = self.mazo
            self.mazo = nodo

    def sacar_arriba(self):
        if self.mazo is None:
            return None
        else:
            carta = self.mazo.dato
            self.mazo = self.mazo.siguiente
            return carta

    def poner_abajo(self, carta):
        nodo = Nodo(carta)
        if self.mazo is None:
            self.mazo = nodo
        else:
            temp = self.mazo
            while temp.siguiente:
                temp = temp.siguiente
            temp.siguiente = nodo

    def quitar_carta(self, carta): #pone la carta del mazo en la mesa
        self.cartas(carta)

    def mezclar(self):
        random.shuffle(self.cartas)
    
    def repartir(self):
        return self.cartas.pop(0)
    
    def __str__(self):
        return str(self.cartas)

class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None

class Carta:
    def __init__(self,valor,palo):
        self.valor = valor
        self.palo = palo

    def __str__(self):
        return self.valor + self.palo

class Juego:
    def __init__(self, seed):
        self.mazo = Mazo()
        self.jugador1 = []
        self.jugador2 = []
        self.turno = 1
        self.max_turnos = 10000
        random.seed(seed)  #Uso una semilla de generación aleatoria para probar distintos escenarios

    def iniciar_juego(self):
        self.mazo.mezclar()
        for _ in range(26):
            self.jugador1.append(self.mazo.repartir())
            self.jugador2.append(self.mazo.repartir())

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

        values = {
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

        carta_jugador1 = self.jugador1.pop(0)
        carta_jugador2 = self.jugador2.pop(0)
        valor_jugador1 = values[carta_jugador1.value]
        valor_jugador2 = values[carta_jugador2.value]

        if carta_jugador1.valor > carta_jugador2.valor:
            print("¡Jugador 1 gana el turno!")
            self.jugador1.append(carta_jugador1)
            self.jugador1.append(carta_jugador2)
        elif carta_jugador1.valor < carta_jugador2.valor:
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

seed = 1234
juego = Juego(seed)
juego.iniciar_juego()

while juego.jugador1 and juego.jugador2 and juego.turno <= juego.max_turnos:
    juego.jugar_turno()

juego.mostrar_resultado()
    
