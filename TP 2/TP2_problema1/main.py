# -*- coding: utf-8 -*-
"""
Sala de emergencias
"""

import time
import datetime
import modulos.paciente as pac
import modulos.monticulo as monticulo
import random

n = 5  # cantidad de ciclos de simulación
cola_de_espera = monticulo.Monticulo()

# Ciclo que gestiona la simulación
for i in range(10):
    # Fecha y hora de entrada de un paciente
    ahora = datetime.datetime.now()
    fecha_y_hora = ahora.strftime('%d/%m/%Y %H:%M:%S')
    print('-*-'*15)
    print('\n', fecha_y_hora, '\n')

    # Se crea un paciente un paciente por segundo
    # La criticidad del paciente es aleatoria
    paciente = pac.Paciente()
    cola_de_espera.agregar(paciente)

    # Atención de paciente en este ciclo: en el 50% de los casos
    if random.random() < 0.5:
        # se atiende paciente que se encuentra al frente de la cola
        paciente_atendido = cola_de_espera.eliminarMin()
        print('*'*10)
        print('Se atiende el paciente:', paciente_atendido)
        print('*'*10)
    else:
        # se continúa atendiendo paciente de ciclo anterior
        pass
    print()

    # Se muestran los pacientes restantes en la cola de espera
    print('Pacientes que faltan atenderse:', cola_de_espera.tamanioActual)
    
    for paciente in cola_de_espera:
        print(paciente)
    
    print()
    print('-*-'*15)
    
    time.sleep(1)