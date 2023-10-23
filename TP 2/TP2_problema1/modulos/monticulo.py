class Monticulo:

    def __init__(self):
        self.listaMonticulo = [0]
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