from files import GestorDatos
from Maximo_peso import BusquedaMax

def main():
    """
    Este programa lee un archivo que contiene información sobre rutas entre ciudades y calcula el
    cuello de botella para cada ruta. Los resultados se imprimen en la consola.
    """
    # Crear una instancia de GestorDatos para manejar la lectura del archivo
    nombre_de_archivo = 'rutas.txt'
    gestor_datos = GestorDatos(nombre_de_archivo)
    datos = gestor_datos.leer_archivo()

    # Calcular distancias desde una ciudad inicial
    ciudad_inicial = 'CiudadBs.As.'

    busqueda_max = BusquedaMax(datos)
    max_cuello_botella, costo_total = busqueda_max.calcular_carga_maxima(ciudad_inicial)

    # Imprimir los resultados

    print('Cuello de botella y costo total desde', ciudad_inicial, 'a cada destino:')
    for ciudad_destino, cuello_botella in max_cuello_botella.items():
        print(ciudad_destino, ':', cuello_botella, 'Costo total:', costo_total[ciudad_destino])

if __name__ == '__main__':
    main()