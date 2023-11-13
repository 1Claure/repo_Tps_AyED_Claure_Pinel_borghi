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
    def __init__(self,fecha_y_hora):
        n = len(nombres)
        self.__nombre = nombres[randint(0, n-1)]
        self.__apellido = apellidos[randint(0, n-1)]
        self.__riesgo = choices(niveles_de_riesgo, probabilidades)[0]
        self.__descripcion = descripciones_de_riesgo[self.__riesgo-1]
        self.__fechayhora =fecha_y_hora
        self.__hora_De_Ingreso = ahora.strftime('%H:%M:%S')

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
        
    def __lt__(self,otro):
        return self.__riesgo < otro.__riesgo
        