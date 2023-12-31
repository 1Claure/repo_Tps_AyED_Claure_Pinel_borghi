class Monticulo:
    """
    Clase que representa un montículo binario.

    Atributos:
    - listaMonticulo: lista que almacena los elementos del montículo.
    - tamanioActual: entero que indica la cantidad de elementos en el montículo.

    Métodos:
    - __iter__(): devuelve un iterador para recorrer los elementos del montículo. O(1)
    - __next__(): devuelve el siguiente elemento del iterador. O(1)
    - agregar(dato): agrega un elemento al montículo y lo acomoda en su posición correspondiente. O(log n)
    - infiltArriba(i): acomoda el elemento en la posición i hacia arriba en el montículo. O(log n)
    - infiltAbajo(i): acomoda el elemento en la posición i hacia abajo en el montículo. O(log n)
    - insertar(k): agrega un elemento al montículo y lo acomoda en su posición correspondiente (mismo método que agregar(dato)). O(log n)
    - hijoMin(i): devuelve el índice del hijo menor del elemento en la posición i. O(1)
    - eliminarMin(): elimina el elemento mínimo del montículo y lo devuelve. O(log n)
    - construirMonticulo(unaLista): construye un montículo a partir de una lista dada. O(n)
    """
    def __init__(self):
        self.listaMonticulo = []
        self.tamanioActual = 0

    def __iter__(self):
       self.aux = 1
       return self
    
    def __next__(self):
       if(self.aux == len(self.listaMonticulo)):
            raise StopIteration
       aux2 = self.listaMonticulo[self.aux]
       self.aux += 1
       return aux2
    
    def agregar(self,dato):
        self.listaMonticulo.append(dato)
        self.tamanioActual = self.tamanioActual + 1
        self.infiltArriba(self.tamanioActual)
    
    def infiltArriba(self,i):
        while i // 2 > 0:
            if self.listaMonticulo[i] < self.listaMonticulo[i // 2]:
                temporal = self.listaMonticulo[i // 2]
                self.listaMonticulo[i // 2] = self.listaMonticulo[i]
                self.listaMonticulo[i] = temporal
            i = i // 2

    def infiltAbajo(self,i):
      while (i * 2) <= self.tamanioActual:
          hm = self.hijoMin(i)
          if self.listaMonticulo[i] > self.listaMonticulo[hm]:
              tmp = self.listaMonticulo[i]
              self.listaMonticulo[i] = self.listaMonticulo[hm]
              self.listaMonticulo[hm] = tmp
          i = hm
    
    def insertar(self,k):
      self.listaMonticulo.append(k)
      self.tamanioActual = self.tamanioActual + 1
      self.infiltArriba(self.tamanioActual)

    def hijoMin(self,i):
      if i * 2 + 1 > self.tamanioActual:
          return i * 2
      else:
          if self.listaMonticulo[i*2] < self.listaMonticulo[i*2+1]:
              return i * 2
          else:
              return i * 2 + 1

    def eliminarMin(self):

        valorSacado = self.listaMonticulo[1]
        self.listaMonticulo[1] = self.listaMonticulo[self.tamanioActual]
        self.tamanioActual = self.tamanioActual - 1
        self.listaMonticulo.pop()
        self.infiltAbajo(1)
        return valorSacado

    def construirMonticulo(self,unaLista):
      i = len(unaLista) // 2
      self.tamanioActual = len(unaLista)
      self.listaMonticulo = [0] + unaLista[:]
      while (i > 0):
          self.infiltAbajo(i)
          i = i - 1

"""
orden de complejidad de cada método de la clase Monticulo:

__init__: Este método inicializa la lista que almacena los elementos del montículo y 
establece el tamaño actual en cero. Como ambas operaciones son de tiempo constante, la complejidad de este método es O(1).

agregar: Este método agrega un elemento al final de la lista y luego lo mueve hacia arriba
hasta que se cumple la propiedad del montículo. El peor caso ocurre cuando el elemento agregado 
es el nuevo mínimo y debe ser movido hasta la raíz del montículo. En este caso, el elemento debe
ser intercambiado con log(n) elementos en el peor de los casos, donde n es el número de elementos en el montículo.
Por lo tanto, la complejidad de este método es O(log n).

eliminar: Este método elimina el elemento mínimo del montículo y lo reemplaza con el último elemento de la lista. 
Luego, el último elemento se mueve hacia abajo hasta que se cumple la propiedad del montículo.
El peor caso ocurre cuando el elemento eliminado es la raíz del montículo y debe ser reemplazado 
por el último elemento de la lista, que luego debe ser movido hacia abajo hasta la hoja más profunda del montículo. 
En este caso, el elemento debe ser intercambiado con log(n) elementos en el peor de los casos, donde n es el número de elementos en el montículo. 
Por lo tanto, la complejidad de este método es O(log n).

es_vacio: Este método simplemente verifica si el tamaño actual del montículo es cero. Como esta operación es de tiempo constante,
la complejidad de este método es O(1).

tamano: Este método devuelve el tamaño actual del montículo. Como esta operación es de tiempo constante, la complejidad
de este método es O(1).

Espero que esto te ayude a entender mejor la complejidad de cada método de la clase Monticulo.¡Por supuesto! Aquí te explico el orden de complejidad de cada método de la clase Monticulo:

__init__: Este método inicializa la lista que almacena los elementos del montículo y establece el tamaño actual en cero. 
Como ambas operaciones son de tiempo constante, la complejidad de este método es O(1).

agregar: Este método agrega un elemento al final de la lista y luego lo mueve hacia arriba hasta que se cumple la 
propiedad del montículo. El peor caso ocurre cuando el elemento agregado es el nuevo mínimo y debe ser movido hasta la raíz del montículo.
En este caso, el elemento debe ser intercambiado con log(n) elementos en el peor de los casos, donde n es el número de elementos en el montículo.
Por lo tanto, la complejidad de este método es O(log n).

eliminar: Este método elimina el elemento mínimo del montículo y lo reemplaza con el último elemento de la lista.
Luego, el último elemento se mueve hacia abajo hasta que se cumple la propiedad del montículo.
El peor caso ocurre cuando el elemento eliminado es la raíz del montículo y debe ser reemplazado por el último
elemento de la lista, que luego debe ser movido hacia abajo hasta la hoja más profunda del montículo.
En este caso, el elemento debe ser intercambiado con log(n) elementos
en el peor de los casos, donde n es el número de elementos en el montículo. Por lo tanto, la complejidad de este método es O(log n).

es_vacio: Este método simplemente verifica si el tamaño actual del montículo es cero. Como esta operación es de tiempo constante,
 la complejidad de este método es O(1).

tamano: Este método devuelve el tamaño actual del montículo. Como esta operación es de tiempo constante,
la complejidad de este método es O(1).

Espero que esto te ayude a entender mejor la complejidad de cada método de la clase Monticulo.

"""