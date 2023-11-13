from monticulo import Monticulo

class GestorDeAtencion:
    def __init__(self):
        self.cola_de_espera = Monticulo()
    
    def agregar_paciente(self, paciente):
        self.cola_de_espera.agregar(paciente)
        
    def atender_paciente(self):
        return self.cola_de_espera.eliminarMin()
        
    def mostrar_pacientes_en_espera(self):
        print('Pacientes que faltan atenderse:', self.cola_de_espera.tamanioActual)
        
        for paciente in self.cola_de_espera:
            print(paciente)
    
    def __str__(self):
        return str(self.cola_de_espera)
    
    def __repr__(self):
        return str(self.cola_de_espera)
    
    def __iter__(self):
        return iter(self.cola_de_espera)