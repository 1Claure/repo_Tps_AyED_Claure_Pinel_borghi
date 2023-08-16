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

    def agregar_al_inicio(self,item): #Agrega un nuevo ítem al inicio de la lista.
        nodoRecorrido = self.cabeza  # Para recorrer los datos
        nuevoNodo = Nodo(item)

        self.largo += 1  # va antes de agregar el nodo para darle su "espacio"
        while nodoRecorrido.nodoAnterior != None :
            nodoRecorrido=nodoRecorrido.nodoAnterior

        nodoRecorrido.nodoAnterior = nuevoNodo
        nuevoNodo.nodoSiguiente = nodoRecorrido


insertar(item, posicion): #Agrega un nuevo ítem a la lista en "posicion". Si la posición no se pasa como argumento, el ítem debe añadirse al final de la lista. "posicion" es un entero que indica la posición en la lista donde se va a insertar el nuevo elemento.

extraer(posicion): #elimina y devuelve el ítem en "posición". Si no se indica el parámetro posición, se elimina y devuelve el último elemento de la lista.

copiar(): #Realiza una copia de la lista elemento a elemento y devuelve la copia.

invertir(): #Invierte el orden de los elementos de la lista.

ordenar(): #Ordena los elementos de la lista de "menor a mayor".

concatenar(Lista): #Recibe una lista como argumento y retorna la lista actual con la lista pasada como parámetro concatenada al final de la primera. Esta operación también debe ser posible utilizando el operador de suma ‘+’. Aclaración: No se deben modificar las listas.
