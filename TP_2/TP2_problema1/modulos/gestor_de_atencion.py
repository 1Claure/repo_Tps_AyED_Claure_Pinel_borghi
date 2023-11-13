from monticulo import Monticulo

class GestorDeAtencion:
    """
    Clase que representa un gestor de atención de pacientes.
    Permite agregar pacientes a una cola de espera y atenderlos en orden de llegada.
    """
    def __init__(self):
        self.cola_de_espera = Monticulo()  # O(1)
    
    def agregar_paciente(self, paciente):
        self.cola_de_espera.agregar(paciente)  # O(log n)
        
    def atender_paciente(self):
        return self.cola_de_espera.eliminarMin()  # O(log n)
        
    def mostrar_pacientes_en_espera(self):
        print('Pacientes que faltan atenderse:', self.cola_de_espera.tamanioActual)  # O(1)
        
        for paciente in self.cola_de_espera:  # O(n)
            print(paciente)  # O(1)
    
    def __str__(self):
        return str(self.cola_de_espera)  # O(n)
    
    def __repr__(self):
        return str(self.cola_de_espera)  # O(n)
    
    def __iter__(self):
        return iter(self.cola_de_espera)  # O(1)
