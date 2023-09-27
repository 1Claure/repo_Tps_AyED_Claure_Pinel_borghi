from juego_guerra import Interfaz

seed = 42091269
juego = Interfaz(seed)
juego.iniciar_juego()
while juego.jugador1 and juego.jugador2 and juego.turno <= juego.max_turnos:
    juego.jugar_turno()

juego.mostrar_resultado()