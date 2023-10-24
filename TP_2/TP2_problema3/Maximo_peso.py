import heapq

class BusquedaMax:
    """
    Una clase que implementa el algoritmo de Dijkstra para encontrar el camino más corto desde un nodo de origen dado a todos los demás nodos en el grafo.
    """

    def __init__(self, datos):
        """
        Inicializa una nueva instancia de la clase BusquedaMax.

        Parámetros:
        - datos: un diccionario que representa el grafo.
        """
        self.datos = datos
    
    def dijkstra(self, origen):
        """
        Aplica el algoritmo de Dijkstra para encontrar el camino más corto desde un nodo de origen dado a todos los demás nodos en el grafo.

        Parámetros:
        - origen: el nodo de origen desde el cual comenzar la búsqueda.

        Devuelve:
        - Un diccionario que contiene el camino más corto desde el nodo de origen a todos los demás nodos en el grafo.
        """
        pesos = {ciudad: float('inf') for ciudad in self.datos}
        pesos[origen] = 0
        heap = [(0, origen)]
        visitados = set()

        while heap:
            (peso, ciudad) = heapq.heappop(heap)
            if ciudad in visitados:
                continue

            visitados.add(ciudad)

            for ciudad_vecina, (peso_actual, costo) in self.datos[ciudad].items():
                nuevo_peso = max(pesos[ciudad], peso_actual)
                if nuevo_peso < pesos[ciudad_vecina]:
                    pesos[ciudad_vecina] = nuevo_peso
                    heapq.heappush(heap, (nuevo_peso, ciudad_vecina))

        return pesos
        
    def calcular_carga_maxima(self, origen):
        """
        Calcula la carga máxima que se puede transportar desde un nodo de origen dado a todos los demás nodos en el grafo.

        Parámetros:
        - origen: el nodo de origen desde el cual comenzar la búsqueda.

        Devuelve:
        - Un diccionario que contiene la carga máxima que se puede transportar desde el nodo de origen a todos los demás nodos en el grafo.
        """
        pesos = {}
        for ciudad in self.datos:
            pesos[ciudad] = float('inf')

        heap = [(0, origen)]
        visitados = set()

        while heap:
            (peso, ciudad) = heapq.heappop(heap)
            if ciudad in visitados:
                continue

            visitados.add(ciudad)

            for ciudad_vecina, (peso_actual, costo) in self.datos[ciudad].items():
                nuevo_peso = min(pesos[ciudad], peso_actual)
                if nuevo_peso < pesos[ciudad_vecina]:
                    pesos[ciudad_vecina] = nuevo_peso
                    heapq.heappush(heap, (-nuevo_peso, ciudad_vecina))

        return pesos
