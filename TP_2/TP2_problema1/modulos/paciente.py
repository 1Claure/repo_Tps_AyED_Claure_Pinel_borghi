from random import randint, choices
import time
import datetime

nombres = ['Leandro', 'Mariela', 'Gastón', 'Andrea', 'Antonio', 'Estela', 'Jorge', 'Agustina']
apellidos = ['Perez', 'Colman', 'Rodriguez', 'Juarez', 'García', 'Belgrano', 'Mendez', 'Lopez']
niveles_de_riesgo = [1, 2, 3]
descripciones_de_riesgo = ['crítico', 'moderado', 'bajo']
ahora = datetime.datetime.now()

# probabilidades de aparición de cada tipo de paciente
probabilidades = [0.1, 0.3, 0.6]

class Paciente:
    """
    Clase que representa a un paciente en un sistema de atención médica.

    Atributos:
    - nombre (str): nombre del paciente.
    - apellido (str): apellido del paciente.
    - riesgo (int): nivel de riesgo del paciente (1, 2 o 3).
    - descripcion (str): descripción del nivel de riesgo del paciente.
    - fechayhora (str): fecha y hora de ingreso del paciente en formato "dd/mm/aaaa hh:mm:ss".
    - hora_De_Ingreso (str): hora de ingreso del paciente en formato "hh:mm:ss".

    Métodos:
    - get_nombre(): devuelve el nombre del paciente. Complejidad O(1).
    - get_apellido(): devuelve el apellido del paciente. Complejidad O(1).
    - get_riesgo(): devuelve el nivel de riesgo del paciente. Complejidad O(1).
    - get_descripcion_riesgo(): devuelve la descripción del nivel de riesgo del paciente. Complejidad O(1).
    - get__hora_De_Ingreso(): devuelve la hora de ingreso del paciente. Complejidad O(1).
    - __str__(): devuelve una cadena con la información del paciente. Complejidad O(1).
    - __lt__(otro): devuelve True si el paciente tiene menor nivel de riesgo que otro paciente, o si tienen el mismo nivel de riesgo pero ingresó antes. De lo contrario, devuelve False. Complejidad O(1).
    """
    def __init__(self,fecha_y_hora):
        n = len(nombres)
        self.__nombre = nombres[randint(0, n-1)]
        self.__apellido = apellidos[randint(0, n-1)]
        self.__riesgo = choices(niveles_de_riesgo, probabilidades)[0]
        self.__descripcion = descripciones_de_riesgo[self.__riesgo-1]
        self.__fechayhora =fecha_y_hora
        self.__hora_De_Ingreso = datetime.datetime.now().strftime('%H:%M:%S')

    def get__hora_De_Ingreso(self):
        return self.__hora_De_Ingreso
    
    def get_nombre(self):
        return self.__nombre
    
    def get_apellido(self):
        return self.__apellido
    
    def get_riesgo(self):
        return self.__riesgo
    
    def get_descripcion_riesgo(self):
        return self.__descripcion

    def __str__(self):
        cad = self.__nombre + ' '
        cad += self.__apellido + ' -> '
        cad += str(self.__riesgo) + '-' + self.__descripcion + ' -> '
        cad += self.__fechayhora
        return cad
        
    def __lt__(self, otro):
        if self.get_riesgo() < otro.get_riesgo():
            return True
        elif self.get_riesgo() > otro.get_riesgo():
            return False
        else:
            return self.get__hora_De_Ingreso() < otro.get__hora_De_Ingreso()
