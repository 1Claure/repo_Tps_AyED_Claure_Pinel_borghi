class Monticulo:
    """
    Clase que representa un montículo binario.
    """

    def __init__(self):
        """
        Inicializa un nuevo montículo vacío.
        """
        self.monticulo = []

    def push(self, item):
        """
        Agrega un elemento al montículo y lo reordena para mantener la propiedad de montículo.
        :param item: El elemento a agregar.
        """
        self.monticulo.append(item)
        self._sift_up(len(self.monticulo) - 1)

    def pop(self):
        """
        Elimina y devuelve el elemento mínimo del montículo, reordenando el montículo para mantener la propiedad de montículo.
        :return: El elemento mínimo del montículo.
        """
        if len(self.monticulo) == 1:
            return self.monticulo.pop()
        else:
            item = self.monticulo[0]
            self.monticulo[0] = self.monticulo.pop()
            self._sift_down(0)
            return item

    def _sift_up(self, i):
        """
        Reordena el montículo hacia arriba a partir del índice dado para mantener la propiedad de montículo.
        :param i: El índice a partir del cual reordenar el montículo hacia arriba.
        """
        padre = (i - 1) // 2
        if i > 0 and self.monticulo[i] < self.monticulo[padre]:
            self.monticulo[i], self.monticulo[padre] = self.monticulo[padre], self.monticulo[i]
            self._sift_up(padre)

    def _sift_down(self, i):
        """
        Reordena el montículo hacia abajo a partir del índice dado para mantener la propiedad de montículo.
        :param i: El índice a partir del cual reordenar el montículo hacia abajo.
        """
        hijo_izquierdo = 2 * i + 1
        hijo_derecho = 2 * i + 2
        minimo = i
        if hijo_izquierdo < len(self.monticulo) and self.monticulo[hijo_izquierdo] < self.monticulo[minimo]:
            minimo = hijo_izquierdo
        if hijo_derecho < len(self.monticulo) and self.monticulo[hijo_derecho] < self.monticulo[minimo]:
            minimo = hijo_derecho
        if minimo != i:
            self.monticulo[i], self.monticulo[minimo] = self.monticulo[minimo], self.monticulo[i]
            self._sift_down(minimo)