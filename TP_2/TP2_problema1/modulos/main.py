import time
import datetime
import paciente as pac
import gestor_de_atencion as gestor
import random

n = 19  # cantidad de ciclos de simulación
gestor_de_atencion = gestor.GestorDeAtencion()

def simulacion():
    """
    Función que simula la atención de pacientes en una clínica.
    Se crean pacientes aleatoriamente y se los agrega a una cola de espera.
    En cada ciclo de simulación se atiende al paciente que se encuentra al frente de la cola.
    """
    for i in range(n):
        # Fecha y hora de entrada de un paciente
        ahora = datetime.datetime.now()
        fecha_y_hora = ahora.strftime('%d/%m/%Y %H:%M:%S')
        print('-*-'*15)
        print('\n', fecha_y_hora, '\n')

        # Se crea un paciente por segundo
        # La criticidad del paciente es aleatoria
        paciente = pac.Paciente(fecha_y_hora)
        gestor_de_atencion.agregar_paciente(paciente)

        # Atención de paciente en este ciclo: en el 50% de los casos
        if random.random() < 0.5:
            # se atiende paciente que se encuentra al frente de la cola
            paciente_atendido = gestor_de_atencion.atender_paciente()

            print('*'*10)
            print('Se atiende el paciente:', paciente_atendido)
            print('*'*10)
        else:
            # se continúa atendiendo paciente de ciclo anterior
            pass
        print()

        # Se muestran los pacientes restantes en la cola de espera
        gestor_de_atencion.mostrar_pacientes_en_espera()

        print()
        print('-*-'*15)

        time.sleep(1)
