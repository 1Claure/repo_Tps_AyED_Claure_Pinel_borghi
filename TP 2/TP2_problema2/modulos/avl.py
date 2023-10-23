from datetime import datetime
from modulos.nodo import TreeNode


class AVL_Tree:
    
    def __init__(self):
        self.raiz = None

    def insert(self, clave, valor):
        self.raiz = self._insert(self.raiz, clave, valor)
    
    def _insert(self, raiz, clave, valor):
        if not raiz:
            return TreeNode(clave, valor)
        elif clave < raiz.clave:
            raiz.hijo_izq = self._insert(raiz.hijo_izq, clave, valor)
            raiz.hijo_izq.padre = raiz
        else:
            raiz.hijo_der = self._insert(raiz.hijo_der, clave, valor)
            raiz.hijo_der.padre = raiz

        # Paso 2: actualice la altura del nodo ancestro
        raiz.altura = 1 + max(self.getaltura(raiz.hijo_izq),
                        self.getaltura(raiz.hijo_der))

        # Paso 3: obtenga el factor de equilibrio
        balance = self.getBalance(raiz)

        # Paso 4: si el nodo está desequilibrado, entonces prueba los 4 casos
        # Caso 1 - Izquierda Izquierda
        if balance > 1 and clave < raiz.hijo_izq.clave:
            return self.hijo_derRotate(raiz)

        # Caso 2 - Derecha Derecha
        if balance < -1 and clave > raiz.hijo_der.clave:
            return self.hijo_izqRotate(raiz)

        # Caso 3 - Izquierda Derecha
        if balance > 1 and clave > raiz.hijo_izq.clave:
            raiz.hijo_izq = self.hijo_izqRotate(raiz.hijo_izq)
            return self.hijo_derRotate(raiz)

        # Caso 4 - Derecha Izquierda
        if balance < -1 and clave < raiz.hijo_der.clave:
            raiz.hijo_der = self.hijo_derRotate(raiz.hijo_der)
            return self.hijo_izqRotate(raiz)

        return raiz

    def delete(self, clave):
        self.raiz = self._delete(self.raiz, clave)
    
    def _delete(self, raiz, clave):
        if not raiz:
            return raiz
        
        elif clave < raiz.clave:
            raiz.hijo_izq = self._delete(raiz.hijo_izq, clave)
        
        elif clave > raiz.clave:
            raiz.hijo_der = self._delete(raiz.hijo_der, clave)
        
        else:
            if raiz.hijo_izq is None:
                temp = raiz.hijo_der
                raiz = None
                if temp:
                    temp.padre = raiz
                return temp
            
            elif raiz.hijo_der is None:
                temp = raiz.hijo_izq
                raiz = None
                if temp:
                    temp.padre = raiz
                return temp
            
            temp = self.getMinValueNode(raiz.hijo_der)
            raiz.clave = temp.clave
            raiz.valor = temp.valor
            raiz.hijo_der = self._delete(raiz.hijo_der, temp.clave)

        # Si el árbol tiene un solo nodo, simplemente devuélvelo
        if raiz is None:
            return raiz

        # Paso 2: actualice la altura del nodo ancestro
        raiz.altura = 1 + max(self.getaltura(raiz.hijo_izq), self.getaltura(raiz.hijo_der))

        # Paso 3: obtenga el factor de equilibrio
        balance = self.getBalance(raiz)

        # Paso 4: si el nodo está desequilibrado, entonces prueba los 4 casos
        # Caso 1 - Izquierda Izquierda
        if balance > 1 and self.getBalance(raiz.hijo_izq) >= 0:
            return self.hijo_derRotate(raiz)

        # Caso 2 - Derecha Derecha
        if balance < -1 and self.getBalance(raiz.hijo_der) <= 0:
            return self.hijo_izqRotate(raiz)

        # Caso 3 - Izquierda Derecha
        if balance > 1 and self.getBalance(raiz.hijo_izq) < 0:
            raiz.hijo_izq = self.hijo_izqRotate(raiz.hijo_izq)
            return self.hijo_derRotate(raiz)

        # Caso 4 - Derecha Izquierda
        if balance < -1 and self.getBalance(raiz.hijo_der) > 0:
            raiz.hijo_der = self.hijo_derRotate(raiz.hijo_der)
            return self.hijo_izqRotate(raiz)

        return raiz

    def hijo_izqRotate(self, z):

        y = z.hijo_der
        T2 = y.hijo_izq

        # Realizar rotación
        y.hijo_izq = z
        y.padre = z.padre
        z.hijo_der = T2
        if T2:  # Actualizar el padre de T2 si T2 existe
            T2.padre = z
        z.padre = y  # Actualizar el padre de z

        # Actualizar alturas
        z.altura = 1 + max(self.getaltura(z.hijo_izq),
                        self.getaltura(z.hijo_der))
        y.altura = 1 + max(self.getaltura(y.hijo_izq),
                        self.getaltura(y.hijo_der))

        # Actualizar el hijo del padre de y
        if y.padre is not None:
            if y.padre.hijo_der == z:
                y.padre.hijo_der = y
            else:
                y.padre.hijo_izq = y

        # Devolver la nueva raíz
        return y

    def hijo_derRotate(self, z):

        y = z.hijo_izq
        T3 = y.hijo_der

        # Realizar rotación
        y.hijo_der = z
        y.padre = z.padre  # Actualizar el padre de y
        z.hijo_izq = T3
        if T3:  # Actualizar el padre de T3 si T3 existe
            T3.padre = z
        z.padre = y  # Actualizar el padre de z

        # Actualizar alturas
        z.altura = 1 + max(self.getaltura(z.hijo_izq),
                            self.getaltura(z.hijo_der))
        y.altura = 1 + max(self.getaltura(y.hijo_izq),
                            self.getaltura(y.hijo_der))

        # Actualizar el hijo del padre de y
        if y.padre is not None:
            if y.padre.hijo_der == z:
                y.padre.hijo_der = y
            else:
                y.padre.hijo_izq = y

        # Devolver la nueva raíz
        return y

    def getaltura(self, nodo):
        if not nodo:
            return 0
        return nodo.altura

    def getBalance(self, nodo):
        if not nodo:
            return 0
        return self.getaltura(nodo.hijo_izq) - self.getaltura(nodo.hijo_der)

    def getMinValueNode(self, nodo):
        current = nodo
        while current.hijo_izq is not None:
            current = current.hijo_izq
        return current
     
    def get(self, clave):
        return self._get(self.raiz, clave)

    def _get(self, raiz, clave):
        if raiz is None:
            return None

        if clave == raiz.clave:
            return raiz.valor

        if clave < raiz.clave:
            return self._get(raiz.hijo_izq, clave)
        else:
            return self._get(raiz.hijo_der, clave)
    
    def max_temp_rango(self, fecha1, fecha2):
        max_temp = float('-inf')

        def in_order_search(nodo_actual):
            nonlocal max_temp
            if nodo_actual:
                if fecha1 <= nodo_actual.clave <= fecha2:
                    max_temp = max(max_temp, nodo_actual.valor)
                if fecha1 <= nodo_actual.clave:
                    in_order_search(nodo_actual.hijo_izq)
                if fecha2 >= nodo_actual.clave:
                    in_order_search(nodo_actual.hijo_der)

        in_order_search(self.raiz)
        return max_temp

    def min_temp_rango(self, fecha1, fecha2):
        min_temp = float('inf') 

        def in_order_search(nodo_actual):
            nonlocal min_temp
            if nodo_actual:
                if fecha1 <= nodo_actual.clave <= fecha2:
                    min_temp = min(min_temp, nodo_actual.valor)
                if fecha1 <= nodo_actual.clave:
                    in_order_search(nodo_actual.hijo_izq)
                if fecha2 >= nodo_actual.clave:
                    in_order_search(nodo_actual.hijo_der)

        in_order_search(self.raiz)
        return min_temp
    
    def temp_extremos_rango(self, fecha1, fecha2):
        min_temp = float('inf')  
        max_temp = float('-inf')  

        def in_order_search(nodo_actual):
            nonlocal min_temp, max_temp
            if nodo_actual:
                if fecha1 <= nodo_actual.clave <= fecha2:
                    min_temp = min(min_temp, nodo_actual.valor)
                    max_temp = max(max_temp, nodo_actual.valor)
                if fecha1 <= nodo_actual.clave:
                    in_order_search(nodo_actual.hijo_izq)
                if fecha2 >= nodo_actual.clave:
                    in_order_search(nodo_actual.hijo_der)

        in_order_search(self.raiz)
        return min_temp, max_temp
    
    def devolver_temperaturas(self, fecha1, fecha2):
        temperaturas = []

        def in_order_search(nodo_actual):
            nonlocal temperaturas
            if nodo_actual:
                if fecha1 <= nodo_actual.clave <= fecha2:
                    temperaturas.append((nodo_actual.clave, nodo_actual.valor))
                if fecha1 <= nodo_actual.clave:
                    in_order_search(nodo_actual.hijo_izq)
                if fecha2 >= nodo_actual.clave:
                    in_order_search(nodo_actual.hijo_der)

        in_order_search(self.raiz)

        # Ordenar la lista de temperaturas por fecha
        temperaturas.sort()

        # Formatear la lista de temperaturas
        temp_sort = []
        for fecha, temperatura in temperaturas:
            temp_sort.append(f"{fecha.day}/{fecha.month}/{fecha.year}: {temperatura} °C")

        return temp_sort
    
    def cantidad_muestras(self):
        cantidad = 0

        def in_order_traversal(nodo_actual):
            nonlocal cantidad
            if nodo_actual:
                cantidad += 1
                in_order_traversal(nodo_actual.hijo_izq)
                in_order_traversal(nodo_actual.hijo_der)

        in_order_traversal(self.raiz)
        return cantidad





















