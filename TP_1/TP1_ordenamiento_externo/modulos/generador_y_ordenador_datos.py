# -*- coding: utf-8 -*-

from random import randint

def crear_archivo_de_datos(nombre):
    f = 10**5
    N = 5*f # 5 millones de datos
    cifras = 20
    tam_bloque = f # 1 M de valores por bloque a escribir
    
    print('Cantidad de valores a escribir:', N)
    
    # truncar archivo si existe
    with open(nombre, 'w') as archivo:
        pass
    
    # escribir datos
    N_restantes = N
    while N_restantes > 0:
        cif = cifras
        r = N_restantes % tam_bloque
        c = N_restantes // tam_bloque
        if c > 0:
            t = tam_bloque
        elif c == 0:
            t = r
        N_restantes -= t
        print('t =', t, ', N_restantes =', N_restantes)
        bloque = [str(randint(10**(cif-1), 10**cif-1))+'\n'
                  for i in range(t)]        
        with open(nombre, 'a+') as archivo:
            archivo.writelines(bloque)

def ordenar_datos(nombre,b):
    
    print('Cantidad de bloques dentro del archivo de texto:', b)

    with open(nombre, 'r') as archivo:
        bloque = archivo.readlines()
    
    contador=0
    
    for line in bloque:
        line.strip()  # Eliminar '\n' 
        contador+=1
    
    bloques_ordenados = []

    with open('ordenado_' + nombre, 'a+') as archivo:
        for i in range(0,contador,b):
            nuevoBloque = bloque [i:(i + b)]
            bloques_ordenados = sorted(nuevoBloque)
            archivo.writelines(bloques_ordenados)

    print("Archivo ordenado con éxito.")

crear_archivo_de_datos('datos.txt')

#ordenar_datos('datos.txt',5)

ordenar_datos('datos.txt',5000000)