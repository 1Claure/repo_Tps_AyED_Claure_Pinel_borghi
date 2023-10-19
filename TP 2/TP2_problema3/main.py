from files import GestorDatos
from Dijkstra import Dijkstra

# Crear una instancia de GestorDatos para gestionar la lectura del archivo
nombre_de_archivo = 'rutas.txt'
gestor_datos = GestorDatos(nombre_de_archivo)
datos = gestor_datos.leer_archivo()

# Crear una instancia de la clase Dijkstra y calcular rutas
dijkstra_algoritmo = Dijkstra(datos)

# Calcular las distancias desde una ciudad inicial
ciudad_inicial = 'CiudadBs.As.'
distancia_minima, distancia_peso_maximo, distancia_costo_minimo = dijkstra_algoritmo.calcular(ciudad_inicial)

# Imprimir los resultados

print('Distancia minima con máximo peso desde', ciudad_inicial, ':')
for ciudad, distancia in distancia_peso_maximo.items():
    print(ciudad, ':', distancia)

print('Distancia mínima y menor costo desde', ciudad_inicial, ':')
for ciudad, distancia in distancia_costo_minimo.items():
    print(ciudad, ':', distancia)