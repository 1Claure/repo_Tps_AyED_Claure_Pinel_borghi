import unittest
import os

class FileTest(unittest.TestCase):

    def test_file_size(self):
        ruta_del_archivo = 'datos.txt'
        ruta_del_archivo_ordenado = 'ordenado_datos.txt'
        if os.path.exists(ruta_del_archivo) and os.path.exists(ruta_del_archivo_ordenado):
           print("Los archivos tienen distinto tamaño.")
        else:
            print("Los archivos tienen el mismo tamaño.")
         

    def test_file_sorted(self): #recorro el archivo para verificar que esté ordenado
        ruta_del_archivo_ordenado = 'ordenado_datos.txt'
        with open(ruta_del_archivo_ordenado, 'r') as archivo:
            bloque = archivo.readlines()
        for line in bloque:
            line.strip()  # Eliminar '\n'


if __name__ == '__main__':
    unittest.main()
 