class Dijkstra:
    def __init__(self, datos):
        self.datos = datos

    def calcular_costo_minimo(self, ciudad_inicial):
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

        
    def calcular_cuello_botella(self, ciudad_inicial):
        visitados = set()

        peso_maximo = {ciudad: float('inf') for ciudad in self.datos}
        peso_maximo[ciudad_inicial] = 0

        while visitados != set(self.datos):
            ciudad_actual = min(self.datos, key=lambda ciudad: peso_maximo[ciudad] if ciudad not in visitados else float('inf'))
            visitados.add(ciudad_actual)

            for ciudad_destino, (peso, costo) in self.datos[ciudad_actual].items():
                if ciudad_destino not in visitados:
                    peso_maximo[ciudad_destino] = max(min(peso_maximo[ciudad_actual], peso), peso_maximo[ciudad_destino])

        return peso_maximo

#La complejidad de tiempo de la función es la misma que la del algoritmo de Dijkstra
#  que es O(N log V) donde N es el número de aristas
#  + V, que es el número de vértices en el grafo.
