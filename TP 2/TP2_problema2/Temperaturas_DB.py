from modulos.avl import AVL_Tree
from datetime import datetime

if __name__ == "__main__":

    def menu():
        
        arbol_avl = AVL_Tree()
        
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
                fecha = datetime.strptime(input("Ingrese la fecha (en formato dd/mm/aaaa): "), '%d/%m/%Y').date()                   
                valor = float(input("Ingrese el valor de temperatura: "))
                arbol_avl.insert(fecha, valor)
            elif opc == 2:
                fecha_bus = datetime.strptime(input("Ingrese la fecha (en formato dd/mm/aaaa): "), '%d/%m/%Y').date()   
                print("La temperatura el {} fue de: {}°C".format(fecha_bus.strftime('%d/%m/%Y'), arbol_avl.get(fecha_bus)))
            elif opc == 3:
                fecha_1 = datetime.strptime(input("Ingrese la primer fecha (en formato dd/mm/aaaa): "), '%d/%m/%Y').date()
                fecha_2 = datetime.strptime(input("Ingrese la segunda fecha (en formato dd/mm/aaaa): "), '%d/%m/%Y').date()                   
                if fecha_1 > fecha_2:
                    fecha_1, fecha_2 = fecha_2, fecha_1
                max_temp = arbol_avl.max_temp_rango(fecha_1, fecha_2)
                print('La temperatura máxima entre {} y {} fue de: {}°C'.format(fecha_1.strftime('%d/%m/%Y'), fecha_2.strftime('%d/%m/%Y'), max_temp))
            elif opc == 4:
                fecha_1 = datetime.strptime(input("Ingrese la primer fecha (en formato dd/mm/aaaa): "), '%d/%m/%Y').date()
                fecha_2 = datetime.strptime(input("Ingrese la segunda fecha (en formato dd/mm/aaaa): "), '%d/%m/%Y').date()
                if fecha_1 > fecha_2:
                    fecha_1, fecha_2 = fecha_2, fecha_1
                min_temp = arbol_avl.min_temp_rango(fecha_1,fecha_2)
                print('La temperatura minima entre {} y {} fue de: {}°C'.format(fecha_1.strftime('%d/%m/%Y'), fecha_2.strftime('%d/%m/%Y'), min_temp))
            elif opc == 5:
                fecha_1 = datetime.strptime(input("Ingrese la primer fecha (en formato dd/mm/aaaa): "), '%d/%m/%Y').date()
                fecha_2 = datetime.strptime(input("Ingrese la segunda fecha (en formato dd/mm/aaaa): "), '%d/%m/%Y').date()
                if fecha_1 > fecha_2:
                    fecha_1, fecha_2 = fecha_2, fecha_1
                min_temp = arbol_avl.min_temp_rango(fecha_1,fecha_2)
                max_temp = arbol_avl.max_temp_rango(fecha_1,fecha_2)
                print('La temperatura minima y maxima entre {} y {} fue de: {}°C y {}°C'.format(fecha_1.strftime('%d/%m/%Y'), fecha_2.strftime('%d/%m/%Y'), min_temp, max_temp))
            elif opc == 6:
                fecha = datetime.strptime(input("Ingrese la fecha (en formato dd/mm/aaaa): "), '%d/%m/%Y').date()
                arbol_avl.delete(fecha)
            elif opc == 7:
                fecha_1 = datetime.strptime(input("Ingrese la primer fecha (en formato dd/mm/aaaa): "), '%d/%m/%Y').date()
                fecha_2 = datetime.strptime(input("Ingrese la segunda fecha (en formato dd/mm/aaaa): "), '%d/%m/%Y').date()
                if fecha_1 > fecha_2:
                    fecha_1, fecha_2 = fecha_2, fecha_1
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
