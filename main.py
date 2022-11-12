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
from snippets.registro import *

# funciones
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
            pass 
        elif opcion == 2:
            os.system('cls')
            registrar() 
 
# main 
if __name__ == '__main__': 

    main()
