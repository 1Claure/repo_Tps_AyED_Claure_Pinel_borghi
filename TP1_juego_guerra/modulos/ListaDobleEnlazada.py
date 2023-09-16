import random

class Nodo:
    def __init__(self,datoInicial):
        self.dato = datoInicial
        self.siguiente = None
        self.anterior = None

    def obtenerDato(self):
        return self.dato

    def obtenerAnterior(self):
        return self.anterior

    def obtenerSiguiente(self):
        return self.siguiente

    def asignarDato(self,nuevodato):
        self.dato = nuevodato

    def asignarSiguiente(self,nuevosiguiente):
        self.siguiente = nuevosiguiente

    def asignarAnterior(self,nuevoanterior):
        self.anterior = nuevoanterior

class ListaDoblementeEnlazada():

    def __init__(self):
        self.cabeza = None
        self.tamanio = 0
        self.cola = None
    
    #sobrecargar el operador [] para que devuelva el elemento en la posición indicada. Si la posición no existe,
    #  debe devolver un IndexError.
    def __getitem__(self, posicion):
        if posicion < 0 or posicion >= self.tamanio:
            raise IndexError("Posicion fuera de rango")
        else:
            nodoRecorrido = self.cabeza
            posicionActual = 0
            while posicionActual < posicion:
                nodoRecorrido = nodoRecorrido.obtenerSiguiente()
                posicionActual += 1
            return nodoRecorrido.dato

    def __len__(self):
        return self.tamanio

    def esta_vacia(self): #Devuelve True si la lista está vacía.
        return self.cabeza == None

    #def tamanio(self): #Devuelve el número de ítems de la lista.
       # return self.tamanio 

    def agregar_al_final(self,item): #Agrega un nuevo ítem al final de la lista.
        nodoRecorrido = self.cabeza #Para recorrer los datos
        nuevoNodo = Nodo (item)
        self.tamanio += 1 #va antes de agregar el nodo para darle su "espacio"

        if nodoRecorrido==None:
            self.cabeza=nuevoNodo
            self.cola=self.cabeza

        else:
            while nodoRecorrido.siguiente != None :
                nodoRecorrido=nodoRecorrido.siguiente
            
            nodoRecorrido.siguiente=nuevoNodo
            nuevoNodo.anterior=nodoRecorrido
            self.cola=nuevoNodo

    def agregar_al_inicio(self,item): #Agrega un nuevo ítem al inicio de la lista.
        nodoRecorrido = self.cabeza  # Para recorrer los datos
        nuevoNodo = Nodo(item)
        self.tamanio += 1  # va antes de agregar el nodo para darle su "espacio"

        if nodoRecorrido==None:
            self.cabeza=nuevoNodo
            self.cola=self.cabeza

        else:
            nodoRecorrido.anterior = nuevoNodo
            nuevoNodo.siguiente = nodoRecorrido
            self.cabeza = nuevoNodo


    #La siguiente función agrega un nuevo ítem a la lista en "posicion"."posicion" es un entero que indica la posición en la lista donde se va a insertar el nuevo elemento. Si la posición no se pasa como argumento, el ítem debe añadirse al final de la lista.
    def insertar(self, item, posicion):
        nuevoNodo = Nodo(item) #Creamos un nuevo objeto de tipo Nodo con el elemento proporcionado y lo almacenamos en la variable nuevoNodo.

        #if nodoRecorrido==None:
            #self.cabeza=nuevoNodo
            #posicion=1

        if posicion is None or posicion >= self.tamanio: #Aquí verificamos si no se proporciona una posición o si la posición proporcionada está fuera del rango actual de la lista.
            self.agregar_al_final(item)  # Agregar al final si no se especifica la posición o si está fuera de rango
            return
        
        if posicion is 0:
            self.agregar_al_inicio(item)
            return
        
        nodoRecorrido = self.cabeza #Inicializamos el nodo de recorrido con el "nodo cabeza"
        posicion_actual = 0 #Inicializamos una variable para realizar un seguimiento de la posición actual mientras recorremos la lista.

        while posicion_actual < posicion: #Usamos un bucle while para avanzar en la lista hasta que alcancemos la posición deseada.
            nodoRecorrido = nodoRecorrido.obtenerSiguiente() #Actualizamos el nodo de recorrido al siguiente nodo en la lista.
            posicion_actual += 1

        anterior = nodoRecorrido.anterior #Obtenemos el nodo anterior al nodo de recorrido.

        nuevoNodo.asignarAnterior(anterior) #Asignamos el nodo anterior al nuevo nodo.
        nuevoNodo.asignarSiguiente(nodoRecorrido) #Asignamos el nodo siguiente al nuevo nodo.
        anterior.siguiente=nuevoNodo #Actualizamos el enlace del nodo anterior para que apunte al nuevo nodo.
        nodoRecorrido.asignarAnterior(nuevoNodo) #Actualizamos el enlace del nodo de recorrido para que apunte al nuevo nodo.
        self.tamanio += 1

    def __str__(self) -> str:
        nodoRecorrido = self.cabeza
        lista = []
        while nodoRecorrido != None:
            lista.append(nodoRecorrido.dato)
            nodoRecorrido = nodoRecorrido.obtenerSiguiente()
        return str(lista)
    
    def __repr__(self) -> str:
        return str(self)

    def extraer(self, posicion=None):
        nodoRecorrido = self.cabeza

        if posicion is None or posicion >= self.tamanio or posicion == -1:
            posicion = self.tamanio - 1

        if posicion == 0:
            if nodoRecorrido is not None:
                na = nodoRecorrido
                self.cabeza = nodoRecorrido.obtenerSiguiente()
                if self.cabeza is not None:
                    self.cabeza.anterior = None
                self.tamanio -= 1
                return na.dato
            else:
                return None

        posicion_actual = 0
        while posicion_actual < posicion:
            nodoRecorrido = nodoRecorrido.obtenerSiguiente()
            posicion_actual += 1

        if nodoRecorrido.anterior is not None:
            nodoRecorrido.anterior.siguiente = nodoRecorrido.siguiente

        if nodoRecorrido.siguiente is not None:
            nodoRecorrido.siguiente.anterior = nodoRecorrido.anterior
        else:
            self.cola = nodoRecorrido.anterior

        self.tamanio -= 1

        return nodoRecorrido.dato


    def copiar(self): #Realiza una copia de la lista elemento a elemento y devuelve la copia  
        nodoRecorrido = self.cabeza
        listaCopia = ListaDoblementeEnlazada()
        while nodoRecorrido != None:
            nuevoNodo = Nodo(nodoRecorrido.dato)
            listaCopia.agregar_al_final(nuevoNodo.dato)
            nodoRecorrido=nodoRecorrido.obtenerSiguiente()
        return listaCopia
    
    def invertir(self): #Invierte el orden de los elementos de la lista.
        na1 = self.cabeza # nodo aux 1
        na2 = self.cola # nodo aux 2

        for _ in range(int(self.tamanio/2)):
            aux = na1.dato
            na1.dato = na2.dato
            na2.dato = aux
            na1 = na1.siguiente
            na2 = na2.anterior


    def ordenar(self): #Ordena los elementos de la lista de "menor a mayor". Se debe utilizar el algoritmo de ordenamiento de insersión.
        nodoRecorrido = self.cabeza
        nodoRecorrido2 = self.cabeza.obtenerSiguiente()
        while nodoRecorrido2 != None:
            while nodoRecorrido != nodoRecorrido2:
                if nodoRecorrido.dato > nodoRecorrido2.dato:
                    aux = nodoRecorrido.dato
                    nodoRecorrido.dato = nodoRecorrido2.dato
                    nodoRecorrido2.dato = aux
                nodoRecorrido = nodoRecorrido.obtenerSiguiente()
            nodoRecorrido2 = nodoRecorrido2.obtenerSiguiente()
            nodoRecorrido = self.cabeza
    
    def desordenar(self):
        nodoRecorrido = self.cabeza
        lista = []

        while nodoRecorrido != None:
            lista.append(nodoRecorrido.dato)
            nodoRecorrido = nodoRecorrido.obtenerSiguiente()

        random.shuffle(lista)

        nodoRecorrido = self.cabeza
        for dato in lista:
            nodoRecorrido.dato = dato
            nodoRecorrido = nodoRecorrido.obtenerSiguiente()

    def concatenar(self,Lista): #Recibe una lista como argumento y retorna la lista actual con la lista pasada como parámetro concatenada al final de la primera. Esta operación también debe ser posible utilizando el operador de suma ‘+’. Aclaración: No se deben modificar las listas.
        nuevaListaConcatenada = self
        
        nodoaAgregar = Lista.cabeza

        while nodoaAgregar is not None:

            nuevaListaConcatenada.agregar_al_final(nodoaAgregar.obtenerDato())
            nodoaAgregar=nodoaAgregar.obtenerSiguiente()

        return nuevaListaConcatenada
    
    def __add__ (self,Lista):

        nuevaListaConcatenada = self.copiar()
        nuevaListaConcatenada.concatenar(Lista)
        return nuevaListaConcatenada
    




