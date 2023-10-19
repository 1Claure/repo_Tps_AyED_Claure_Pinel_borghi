class Dijkstra:
    def __init__(self, datos):
        self.datos = datos

    def calcular(self, ciudad_inicial):
        visitados = set()
        
        distancia_minima = {ciudad: float('inf') for ciudad in self.datos}
        distancia_peso_maximo = {ciudad: 0 for ciudad in self.datos}
        distancia_costo_minimo = {ciudad: float('inf') for ciudad in self.datos}
        
        distancia_minima[ciudad_inicial] = 0
        distancia_costo_minimo[ciudad_inicial] = 0
        
        while visitados != set(self.datos):
            ciudad_actual = min(self.datos, key=lambda ciudad: (distancia_minima[ciudad], distancia_costo_minimo[ciudad]) if ciudad not in visitados else (float('inf'), float('inf')))
            visitados.add(ciudad_actual)

            for ciudad_destino, (peso, costo) in self.datos[ciudad_actual].items():
                if ciudad_destino not in visitados:
                    distancia_minima[ciudad_destino] = min(distancia_minima[ciudad_actual] + peso, distancia_minima[ciudad_destino])
                    distancia_peso_maximo[ciudad_destino] = max(distancia_peso_maximo[ciudad_actual], peso)
                    distancia_costo_minimo[ciudad_destino] = min(distancia_costo_minimo[ciudad_actual] + costo, distancia_costo_minimo[ciudad_destino])
        
        return distancia_minima, distancia_peso_maximo, distancia_costo_minimo