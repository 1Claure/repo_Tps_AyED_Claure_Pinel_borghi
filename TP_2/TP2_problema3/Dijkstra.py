class Dijkstra:
    def __init__(self, datos):
        """
        Constructor de la clase Dijkstra.

        :param datos: Diccionario que representa el grafo con sus pesos y costos.
        """
        self.datos = datos

    def calcular_costo_minimo(self, ciudad_inicial):
        """
        Calcula el costo mínimo para llegar a cada ciudad desde la ciudad inicial.

        :param ciudad_inicial: Ciudad de origen.
        :return: Diccionario con las distancias mínimas a cada ciudad.
        """
        visitados = set()
        
        distancia_minima = {ciudad: float('inf') for ciudad in self.datos}
        distancia_minima[ciudad_inicial] = 0
        
        while visitados != set(self.datos):
            ciudad_actual = min(self.datos, key=lambda ciudad: distancia_minima[ciudad] if ciudad not in visitados else float('inf'))
            visitados.add(ciudad_actual)

            for ciudad_destino, (peso, costo) in self.datos[ciudad_actual].items():
                if ciudad_destino not in visitados:
                    distancia_minima[ciudad_destino] = min(distancia_minima[ciudad_actual] + costo, distancia_minima[ciudad_destino])

        return distancia_minima

#La complejidad de tiempo de la función es la misma que la del algoritmo de Dijkstra
#  que es O(N log V) donde N es el número de aristas
#  + V, que es el número de vértices en el grafo.
