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



# funciones
def menu_login(username): 

    menu_login = f"""
    Bienvenido, {username}. 
    
    Seleccione opción (-1 para desloguear): """

    while True: 
        os.system("cls")
        opcion = int(input(menu_login))
    
        if opcion == -1: 
            break 
    
def main(): 

    menu_principal = """
    Bienvenido. 

    1 - Ingresar
    2 - Registrarse 

    Seleccione una opción (-1 para salir): """
    
    while True: 
        os.system('cls')
        opcion = int(input(menu_principal))

        if opcion == -1: 
            break 
        elif opcion == 1: 
            logueado = login() # login retorna el nombre del usuario validado, en caso de que la pw sea correcta. 
            # si hay un nombre de usuario, se lo pasamos a la función menú login. 
            if logueado: 
                menu_login(logueado)
        elif opcion == 2:
            registrar() 
 
nombre_cuenta = False 

# main 
if __name__ == '__main__': 

    main()
    