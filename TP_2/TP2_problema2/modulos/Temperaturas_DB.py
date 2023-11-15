from Arbol_AVL import AVL_Tree
import datetime

class TemperaturasDB:
   def __init__(self):
       self.db = AVL_Tree()

   def guardar_temperatura(self, temperatura, fecha):
    self.db.raiz = self.db._insert(self.db.raiz, fecha, temperatura)

   def devolver_temperatura(self, fecha):
        return self.db._get(self.db.raiz, fecha)

   def max_temp_rango(self, fecha1, fecha2):
        max_temp = float('-inf')

        def callback(nodo):
            nonlocal max_temp
            if fecha1 <= nodo.clave <= fecha2:
                max_temp = max(max_temp, nodo.valor)

        self.db.in_order_traversal(self.db.raiz, callback)

        return max_temp
   
   def min_temp_rango(self, fecha1, fecha2):
        min_temp = float('inf') 

        def callback(nodo):
            nonlocal min_temp
            if fecha1 <= nodo.clave <= fecha2:
                min_temp = min(min_temp, nodo.valor)

        self.db.in_order_traversal(self.db.raiz, callback)

        return min_temp

   def temp_extremos_rango(self, fecha1, fecha2):
        min_temp = float('inf')  
        max_temp = float('-inf')  

        def callback(nodo):
            nonlocal min_temp, max_temp
            if fecha1 <= nodo.clave <= fecha2:
                min_temp = min(min_temp, nodo.valor)
                max_temp = max(max_temp, nodo.valor)

        self.db.in_order_traversal(self.db.raiz, callback)

   def borrar_temperatura(self, fecha):
       self.db.raiz = self.db._delete(self.db.raiz, fecha)
   
   def devolver_temperaturas(self, fecha1, fecha2):
        temperaturas = []

        def callback(nodo):
            nonlocal temperaturas
            if fecha1 <= nodo.clave <= fecha2:
                temperaturas.append((nodo.clave, nodo.valor))

        self.db.in_order_traversal(self.db.raiz, callback)

        # Ordenar la lista de temperaturas por fecha
        temperaturas.sort()

        # Formatear la lista de temperaturas
        temp_sort = []
        for fecha, temperatura in temperaturas:
            temp_sort.append(f"{fecha.day}/{fecha.month}/{fecha.year}: {temperatura} °C")

        return temp_sort

   def cantidad_muestras(self):
        cantidad = 0
        def callback(nodo):
            nonlocal cantidad
            cantidad += 1
        self.db.in_order_traversal(self.db.raiz, callback)

        return cantidad
