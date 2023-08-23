class Nodo:
    def __init__(self,datoInicial):
        self.dato = datoInicial
        self.nodoSiguiente = None
        self.nodoAnterior = None

    def obtenerDato(self):
        return self.dato

    def obtenerAnterior(self):
        return self.nodoAnterior

    def obtenerSiguiente(self):
        return self.nodoSiguiente

    def asignarDato(self,nuevodato):
        self.dato = nuevodato

    def asignarSiguiente(self,nuevosiguiente):
        self.nodoSiguiente = nuevosiguiente

    def asignarAnterior(self,nuevoanterior):
        self.nodoAnterior = nuevoanterior

class ListaDoblementeEnlazada():

    def __init__(self):
        self.cabeza = None
        self.largo = 0
        self.cola = None

    def esta_vacia(self): #Devuelve True si la lista está vacía.
        return self.cabeza == None

    def tamanio(self): #Devuelve el número de ítems de la lista.
        return self.largo

    def agregar_al_final(self,item): #Agrega un nuevo ítem al final de la lista.
        nodoRecorrido = self.cabeza #Para recorrer los datos
        nuevoNodo = Nodo (item)

        self.largo += 1 #va antes de agregar el nodo para darle su "espacio"
        while nodoRecorrido.nodoSiguiente != None :
            nodoRecorrido=nodoRecorrido.nodoSiguiente

        nodoRecorrido.nodoSiguiente=nuevoNodo
        nuevoNodo.nodoAnterior=nodoRecorrido
        self.cola=nuevoNodo

    def agregar_al_inicio(self,item): #Agrega un nuevo ítem al inicio de la lista.
        nodoRecorrido = self.cabeza  # Para recorrer los datos
        nuevoNodo = Nodo(item)

        self.largo += 1  # va antes de agregar el nodo para darle su "espacio"
        while nodoRecorrido.nodoAnterior != None :
            nodoRecorrido=nodoRecorrido.nodoAnterior

        nodoRecorrido.nodoAnterior = nuevoNodo
        nuevoNodo.nodoSiguiente = nodoRecorrido


    #La siguiente función agrega un nuevo ítem a la lista en "posicion"."posicion" es un entero que indica la posición en la lista donde se va a insertar el nuevo elemento. Si la posición no se pasa como argumento, el ítem debe añadirse al final de la lista.
    def insertar(self, item, posicion=None):
        nuevoNodo = Nodo(item) #Creamos un nuevo objeto de tipo Nodo con el elemento proporcionado y lo almacenamos en la variable nuevoNodo.

        if posicion is None or posicion >= self.largo: #Aquí verificamos si no se proporciona una posición o si la posición proporcionada está fuera del rango actual de la lista.
            self.agregar_al_final(item)  # Agregar al final si no se especifica la posición o si está fuera de rango
            return

        nodoRecorrido = self.cabeza #Inicializamos el nodo de recorrido con el "nodo cabeza"
        posicion_actual = 0 #Inicializamos una variable para realizar un seguimiento de la posición actual mientras recorremos la lista.

        while posicion_actual < posicion: #Usamos un bucle while para avanzar en la lista hasta que alcancemos la posición deseada.
            nodoRecorrido = nodoRecorrido.obtenerSiguiente() #Actualizamos el nodo de recorrido al siguiente nodo en la lista.
            posicion_actual += 1

        nodoAnterior = nodoRecorrido.obtenerAnterior() #Obtenemos el nodo anterior al nodo de recorrido.

        nuevoNodo.asignarAnterior(nodoAnterior) #Asignamos el nodo anterior al nuevo nodo.
        nuevoNodo.asignarSiguiente(nodoRecorrido) #Asignamos el nodo siguiente al nuevo nodo.
        nodoAnterior.asignarSiguiente(nuevoNodo) #Actualizamos el enlace del nodo anterior para que apunte al nuevo nodo.
        nodoRecorrido.asignarAnterior(nuevoNodo) #Actualizamos el enlace del nodo de recorrido para que apunte al nuevo nodo.
        self.largo += 1

    def extraer(self,item,posicion): #elimina y devuelve el ítem en "posición". Si no se indica el parámetro posición, se elimina y devuelve el último elemento de la lista.
        nodoRecorrido=self.cabeza
        
        if posicion is None:
            posicion=self.largo-1
        
        posicionActual=0

        while(posicion > posicionActual):
            nodoRecorrido=nodoRecorrido.obtenerSiguiente()
            posicionActual+=1

        dato_anterior=nodoRecorrido.nodoAnterior
        dato_anterior.nodoSiguiente = nodoRecorrido.nodoSiguiente

        dato_siguiente=nodoRecorrido.nodoSiguiente
        dato_siguiente.nodoAnterior = nodoRecorrido.nodoAnterior

        nodoAExtraer = nodoRecorrido
        nodoAExtraer.nodoSiguiente = None
        nodoAExtraer.nodoAnterior = None
        
        return nodoAExtraer.dato


    def copiar(self): #Realiza una copia de la lista elemento a elemento y devuelve la copia
        nodoRecorrido = self.cabeza
        listaCopia = ListaDoblementeEnlazada()
        while nodoRecorrido != None:
            nuevoNodo = Nodo(nodoRecorrido.dato)
            listaCopia.agregar_al_final(nuevoNodo.dato)
            nodoRecorrido=nodoRecorrido.obtenerSiguiente()
        return listaCopia
    
    def invertir(): #Invierte el orden de los elementos de la lista.
        nodoRecorrido = self.cabeza
        listaCopia = ListaDoblementeEnlazada()

ordenar(): #Ordena los elementos de la lista de "menor a mayor".

concatenar(Lista): #Recibe una lista como argumento y retorna la lista actual con la lista pasada como parámetro concatenada al final de la primera. Esta operación también debe ser posible utilizando el operador de suma ‘+’. Aclaración: No se deben modificar las listas.
