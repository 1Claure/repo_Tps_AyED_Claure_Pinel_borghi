from monticulo import Monticulo

class BusquedaMax:
    def __init__(self, datos):
        """
        Inicializa la clase BusquedaMax con los datos de entrada.

        Args:
        - datos (dict): Un diccionario que representa los datos de entrada.
        """
        self.datos = datos

    def calcular_carga_maxima(self, origen):
        """
        Calcula la carga máxima que se puede transportar desde el origen a cada ciudad y su respectivo coste.

        Args:
        - origen (str): El nombre de la ciudad de origen.

        Returns:
        - cuello_botella (dict): Un diccionario que representa la carga máxima que se puede transportar desde el origen a cada ciudad.
        - costo_total (dict): Un diccionario que representa el costo total de transporte desde el origen a cada ciudad.
        """
        cuello_botella = {ciudad: 0 for ciudad in self.datos}
        costo_total = {ciudad: float('inf') for ciudad in self.datos}
        camino = {ciudad: [] for ciudad in self.datos}
        cuello_botella[origen] = float('inf')
        costo_total[origen] = 0
        cola = Monticulo()
        cola.push((-float('inf'), origen))
        
        while cola.monticulo:
            peso, ciudad_actual = cola.pop()
            peso *= -1

            for ciudad_destino, (peso_arista, costo_arista) in self.datos[ciudad_actual].items():
                min_peso = min(peso, peso_arista)
                nuevo_costo = costo_total[ciudad_actual] + costo_arista
                if min_peso > cuello_botella[ciudad_destino] or (min_peso == cuello_botella[ciudad_destino] and nuevo_costo < costo_total[ciudad_destino]):
                    cuello_botella[ciudad_destino] = min_peso
                    costo_total[ciudad_destino] = nuevo_costo
                    camino[ciudad_destino] = camino[ciudad_actual] + [ciudad_destino]
                    cola.push((-min_peso, ciudad_destino))
        
        return cuello_botella, costo_total