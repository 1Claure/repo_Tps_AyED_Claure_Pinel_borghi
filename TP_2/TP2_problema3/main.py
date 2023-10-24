from files import GestorDatos
from Dijkstra import Dijkstra
from Maximo_peso import BusquedaMax

def main():
    """
    Este programa lee un archivo que contiene información sobre rutas entre ciudades y calcula la distancia más corta
    y el costo mínimo desde una ciudad de inicio dada utilizando el algoritmo de Dijkstra. También calcula la ciudad
    cuello de botella para cada ruta. Los resultados se imprimen en la consola.
    """
    # Crear una instancia de GestorDatos para manejar la lectura del archivo
    nombre_de_archivo = 'TP_2\TP2_problema3\rutas.txt'
    gestor_datos = GestorDatos(nombre_de_archivo)
    datos = gestor_datos.leer_archivo()

    # Crear una instancia de la clase Dijkstra y calcular las rutas
    dijkstra_algoritmo = Dijkstra(datos)

    # Calcular distancias desde una ciudad inicial
    ciudad_inicial = 'CiudadBs.As.'
    distancia_costo_minimo = dijkstra_algoritmo.calcular_costo_minimo(ciudad_inicial)

    busqueda_max = BusquedaMax(datos)
    max_cuello_botella = busqueda_max.calcular_carga_maxima(ciudad_inicial)

    # Imprimir los resultados

    print('Distancia mínima y menor costo desde', ciudad_inicial, ':')
    for ciudad, distancia in distancia_costo_minimo.items():
        print(ciudad, ':', distancia)


    print('Cuello de botella desde', ciudad_inicial, 'a cada destino:')
    for ciudad_destino, cuello_botella in max_cuello_botella.items():
        print(ciudad_destino, ':', cuello_botella)

if __name__ == '__main__':
    main()
