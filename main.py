# -*- coding: utf-8 -*-
#
#  main.py
#  
#  Trabajo Práctico Final
#  Algoritmos y Estructuras de Datos I
#  Equipo: Cañete Andrés, Ciardelli Martín, Touris Santiago, Traba Federico, Zarate Lautaro

# librerias
import os

# módulos propios
from snippets.registro import registrar
from snippets.login import login
from snippets.fechas import agregar_fecha, matriz_fechas, mostrar_fechas, modificar_fechas, id_fecha, eliminar_fechas

# funciones
def mostrar_opciones(username): 
    fechas = matriz_fechas(username)
    
    print(f"Hola de nuevo, {username}.\nTenés {len(fechas)} fechas de exámenes activas\n")

    mostrar_fechas(fechas)

    print("\n1. Agregar nueva fecha.\n2. Modificar fecha.\n3. Eliminar fecha.")

    return 


def menu_login(username): 

    while True: 
        os.system("cls")
        mostrar_opciones(username)
        opcion = int(input(f"\nSeleccione una opción (-1 para desloguear):"))
        if opcion == -1: 
            break 
        elif opcion == 1:
            agregar_fecha(username)
        elif opcion == 2:
            modificar_fechas(id_fecha((matriz_fechas(username))),matriz_fechas(username), username)
            mostrar_opciones(username)
        elif opcion == 3:
            eliminar_fechas(id_fecha(matriz_fechas(username)), matriz_fechas(username), username)


    return 

def main(): 

    menu = ('Bienvenido.', '\n1. Ingresar', "2. Registrarse")
    
    while True: 
        os.system('cls')
        
        [print(element) for element in menu]
        opcion = int(input("\nSeleccione una opción (-1 para salir): "))

        if opcion == -1: 
            break 
        elif opcion == 1: 
            logueado = login() # login retorna el nombre del usuario validado, en caso de que la pw sea correcta. 
            # si hay un nombre de usuario, se lo pasamos a la función menú login. 
            if logueado: 
                menu_login(logueado)
        elif opcion == 2:
            registrar() 

    return 
    
# main 
if __name__ == '__main__': 

    main()
    