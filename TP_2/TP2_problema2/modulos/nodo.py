class TreeNode:
    def __init__(self, clave, valor):
        self.clave = clave
        self.valor = valor
        self.hijo_izq = None
        self.hijo_der = None
        self.padre = None
        self.altura = 1