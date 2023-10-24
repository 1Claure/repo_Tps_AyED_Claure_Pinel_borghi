from modulos.avl import AVL_Tree
from datetime import datetime

if __name__ == "__main__":

    def menu():
        
        arbol_avl = AVL_Tree()
        # Dataset de prueba
        datos_prueba = [
            ('01/01/2021', 25.0),
            ('02/01/2021', 26.0),
            ('03/01/2021', 27.0),
            ('04/01/2021', 28.0),
            ('05/01/2021', 29.0),
            ('06/01/2021', 30.0),
            ('07/01/2021', 31.0),
            ('08/01/2021', 32.0),
            ('09/01/2021', 33.0),
            ('10/01/2021', 34.0),
            ('11/01/2021', 35.0),
            ('12/01/2021', 36.0),
            ('13/01/2021', 37.0),
            ('14/01/2021', 38.0),
            ('15/01/2021', 39.0),
            ('16/01/2021', 40.0),
            ('17/01/2021', 41.0),
            ('18/01/2021', 42.0),
            ('19/01/2021', 43.0),
            ('20/01/2021', 44.0),
            ('21/01/2021', 45.0),
            ('22/01/2021', 46.0),
            ('23/01/2021', 47.0),
            ('24/01/2021', 48.0),
            ('25/01/2021', 49.0),
            ('26/01/2021', 50.0),
            ('27/01/2021', 51.0),
            ('28/01/2021', 52.0),
        ]
        
        for fecha, valor in datos_prueba:
            fecha = datetime.strptime(fecha, '%d/%m/%Y').date()
            arbol_avl.insert(fecha, valor)
        
        while True:
            print("\nÁrbol AVL\n"
                    + "\n\t1. Ingresar temperatura"
                    + "\n\t2. Devolver temperatura"
                    + "\n\t3. Maxima temperatura entre dos fechas"
                    + "\n\t4. Minima temperatura entre dos fechas"
                    + "\n\t5. Temperatura minima y maxima entre dos fechas"
                    + "\n\t6. Eliminar temperatura"
                    + "\n\t7. Mostar temperaturas entre dos fechas"
                    + "\n\t8. Cantidad de muestras"
                    + "\n\t9. Salir")

            try:
                opc = int(input("Ingrese su opción "))
            except ValueError:
                print("Ingresaste una opcion erronea. Por favor, ingresa un numero.")
                continue

            if opc == 1:
                while True:
                    try:
                        fecha = datetime.strptime(input("Ingrese la fecha (en formato dd/mm/aaaa): "), '%d/%m/%Y').date()                   
                        valor = float(input("Ingrese el valor de temperatura: "))
                        break
                    except ValueError:
                        print("Ingresaste un valor de temperatura o fecha invalido. Por favor, ingresa un valor numerico para la temperatura y una fecha valida en formato dd/mm/aaaa.")
                        continue
                arbol_avl.insert(fecha, valor)
            elif opc == 2:
                while True:
                    try:
                        fecha_bus = datetime.strptime(input("Ingrese la fecha (en formato dd/mm/aaaa): "), '%d/%m/%Y').date()   
                        break
                    except ValueError:
                        print("Ingresaste una fecha invalida. Por favor, ingresa una fecha valida en formato dd/mm/aaaa.")
                        continue
                print("La temperatura el {} fue de: {}°C".format(fecha_bus.strftime('%d/%m/%Y'), arbol_avl.get(fecha_bus)))
            elif opc == 3:
                while True:
                    try:
                        fecha_1 = datetime.strptime(input("Ingrese la primer fecha (en formato dd/mm/aaaa): "), '%d/%m/%Y').date()
                        fecha_2 = datetime.strptime(input("Ingrese la segunda fecha (en formato dd/mm/aaaa): "), '%d/%m/%Y').date()                   
                        if fecha_1 > fecha_2:
                            fecha_1, fecha_2 = fecha_2, fecha_1
                        break
                    except ValueError:
                        print("Ingresaste una fecha invalida. Por favor, ingresa una fecha valida en formato dd/mm/aaaa.")
                        continue
                max_temp = arbol_avl.max_temp_rango(fecha_1, fecha_2)
                print('La temperatura máxima entre {} y {} fue de: {}°C'.format(fecha_1.strftime('%d/%m/%Y'), fecha_2.strftime('%d/%m/%Y'), max_temp))
            elif opc == 4:
                while True:
                    try:
                        fecha_1 = datetime.strptime(input("Ingrese la primer fecha (en formato dd/mm/aaaa): "), '%d/%m/%Y').date()
                        fecha_2 = datetime.strptime(input("Ingrese la segunda fecha (en formato dd/mm/aaaa): "), '%d/%m/%Y').date()
                        if fecha_1 > fecha_2:
                            fecha_1, fecha_2 = fecha_2, fecha_1
                        break
                    except ValueError:
                        print("Ingresaste una fecha invalida. Por favor, ingresa una fecha valida en formato dd/mm/aaaa.")
                        continue
                min_temp = arbol_avl.min_temp_rango(fecha_1,fecha_2)
                print('La temperatura minima entre {} y {} fue de: {}°C'.format(fecha_1.strftime('%d/%m/%Y'), fecha_2.strftime('%d/%m/%Y'), min_temp))
            elif opc == 5:
                while True:
                    try:
                        fecha_1 = datetime.strptime(input("Ingrese la primer fecha (en formato dd/mm/aaaa): "), '%d/%m/%Y').date()
                        fecha_2 = datetime.strptime(input("Ingrese la segunda fecha (en formato dd/mm/aaaa): "), '%d/%m/%Y').date()
                        if fecha_1 > fecha_2:
                            fecha_1, fecha_2 = fecha_2, fecha_1
                        break
                    except ValueError:
                        print("Ingresaste una fecha invalida. Por favor, ingresa una fecha valida en formato dd/mm/aaaa.")
                        continue
                min_temp = arbol_avl.min_temp_rango(fecha_1,fecha_2)
                max_temp = arbol_avl.max_temp_rango(fecha_1,fecha_2)
                print('La temperatura minima y maxima entre {} y {} fue de: {}°C y {}°C'.format(fecha_1.strftime('%d/%m/%Y'), fecha_2.strftime('%d/%m/%Y'), min_temp, max_temp))
            elif opc == 6:
                while True:
                    try:
                        fecha = datetime.strptime(input("Ingrese la fecha (en formato dd/mm/aaaa): "), '%d/%m/%Y').date()
                        break
                    except ValueError:
                        print("Ingresaste una fecha invalida. Por favor, ingresa una fecha valida en formato dd/mm/aaaa.")
                        continue
                arbol_avl.delete(fecha)
            elif opc == 7:
                while True:
                    try:
                        fecha_1 = datetime.strptime(input("Ingrese la primer fecha (en formato dd/mm/aaaa): "), '%d/%m/%Y').date()
                        fecha_2 = datetime.strptime(input("Ingrese la segunda fecha (en formato dd/mm/aaaa): "), '%d/%m/%Y').date()
                        if fecha_1 > fecha_2:
                            fecha_1, fecha_2 = fecha_2, fecha_1
                        break
                    except ValueError:
                        print("Ingresaste una fecha invalida. Por favor, ingresa una fecha valida en formato dd/mm/aaaa.")
                        continue
                temperaturas = arbol_avl.devolver_temperaturas(fecha_1,fecha_2)
                for temperatura in temperaturas:
                    print(temperatura)
            elif opc == 8:                                        
                print(arbol_avl.cantidad_muestras())                   
            elif opc == 9:                                      
                print("Adios")
                break 
            else:
                print("Ingresaste una opción errónea")
    

    menu()