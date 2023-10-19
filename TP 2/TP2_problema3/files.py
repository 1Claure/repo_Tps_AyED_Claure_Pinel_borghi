class GestorDatos:
    def __init__(self, nombre_archivo):
        self.nombre_archivo = nombre_archivo
        self.ciudades = self.leer_archivo()

    def leer_archivo(self):
        datos = {}
        with open(self.nombre_archivo, 'r') as archivo:
            lineas = archivo.readlines()

        for linea in lineas:
            partes = linea.strip().split(',')
            if len(partes) >= 4:
                nombre1, nombre2, peso, costo = partes[0], partes[1], int(partes[2]), int(partes[3])
                print(partes[0], partes[1], partes[2], partes[3])
                if nombre1 not in datos:
                    datos[nombre1] = {}
                if nombre2 not in datos:
                    datos[nombre2] = {}

                datos[nombre1][nombre2] = (peso, costo)
        return datos
