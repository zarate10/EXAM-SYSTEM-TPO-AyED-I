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
from snippets.fechas import agregar_fecha, matriz_fechas, mostrar_fechas

# funciones
def mostrar_opciones(username): 
    fechas = matriz_fechas(username)
    
    logueado = (f"Hola de nuevo, {username}.", f"Tenés {len(fechas)} fechas de exámenes activas\n")
    [print(element) for element in logueado]

    mostrar_fechas(fechas)

    opciones = ("\n1. Agregar nueva fecha.", "2. Modificar fecha.", "3. Eliminar fecha.")
    [print(element) for element in opciones]

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
    