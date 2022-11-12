# -*- coding: utf-8 -*-
#
#  main.py
#  
#  Copyright 2022 by Diógenes y los perros
#  Equipo: Cañete Andrés, Ciardelli Martín, Touris Santiago, Traba Federico, Zarate Lautaro

import os

# módulos propios
from registro import * 

def main(): 

    menu_principal = """
    Bienvenido. 

    1 - Ingresar
    2 - Registrarse 

    Seleccione una opción (-1 para salir): """
    
    opcion = int(input(menu_principal))
    
    while True: 

        if opcion == -1: 
            break 
        elif opcion == 1: 
            pass 
        elif opcion == 2:
            pass 

if __name__ == '__main__': 

    main()
