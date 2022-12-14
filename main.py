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
from snippets.fechas import agregar_fecha, matriz_fechas, fechas_user, modificar_fechas, id_fecha, eliminar_fechas, arr_dias_restantes

# funciones
def borrar_pantalla():
    '''Limpia la pantalla'''    
    os.system('cls' if os.name == 'nt' else 'clear')
    return

def mostrar_opciones(fechas, username, ordenar): 

    print(f"Hola de nuevo, {username}.\nTenés {len(matriz_fechas(username))} fechas de exámenes activas\n")

    if len(fechas) != 0: 
        fechas_user(fechas, ordenar)

    print("\n1. Agregar nueva fecha.\n2. Modificar registro.\n3. Ordenar fechas x días restantes.\n4. Eliminar fecha.")

    return 

def menu_login(username): 
    error = False 
    ordenado = False 

    while True: 
        fechas = matriz_fechas(username)
        borrar_pantalla()
        mostrar_opciones(fechas, username, ordenado)

        if error: 
            print('Ocurrió algo inesperado.\n')
            error = False
        try: 
            opcion = int(input(f"\nSeleccione una opción (-1 para desloguear):"))
        except (EOFError, KeyboardInterrupt):
            print('')
            quit()
        except Exception as e:
            error = True 
        else: 
            if opcion == -1: 
                break 
            elif opcion == 1:
                agregar_fecha(username)
            elif opcion == 2:
                modificar_fechas(id_fecha(fechas), fechas, username)
                mostrar_opciones(fechas, username, ordenado)
            elif opcion == 3:
                ordenado = True
                mostrar_opciones(fechas, username, ordenado)
            elif opcion == 4:
                eliminar_fechas(id_fecha(fechas), fechas, username)
    return 

def main(): 
    error = False 

    while True: 
        borrar_pantalla()

        if error: 
            print('Ocurrió algo inesperado.\n')
            error = False

        try: 
            print('Bienvenido.\n \n1. Ingresar\n2. Registrarse')
            opcion = int(input("\nSeleccione una opción (-1 para salir): "))
        
        except (KeyboardInterrupt, EOFError):
            print('')
            quit()
        except Exception as e: 
            error = True
        else: 
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
    