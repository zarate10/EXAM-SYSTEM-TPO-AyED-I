# -*- coding: utf-8 -*-
#
#  login.py
#  
#  Trabajo Práctico Final
#  Algoritmos y Estructuras de Datos I
#  Equipo: Cañete Andrés, Ciardelli Martín, Touris Santiago, Traba Federico, Zarate Lautaro

import os
from snippets.registro import usuario_existe

sep = os.path.sep
dir_actual = os.path.dirname(os.path.abspath(__file__))
dir = sep.join(dir_actual.split(sep)[:-1])

path_users = dir + '/db/usuarios'
usuarios = os.scandir(path_users)

def login():
    """
    Función para iniciar sesión en main. 
    Si se encuentra el usuario, se tienen 3 intentos para ingresar la contraseña correcta. 
    Caso contrario se devuelve al menu
    Precondición: n/a 
    Postcondición: Valida user y lo devuelve para mantener sesión, caso contrario retorna False.
    """
    
    intentos = 0
    while True:
        try: 
            user = input('\nIngrese su usuario (-1 para salir): ')
        except (KeyboardInterrupt, EOFError):
            print('')
            quit()
        except Exception as e: 
            print('Ocurrió un error inesperado.')
        else: 
            if user == '-1':
                return False
            else:
                if usuario_existe(user, path_users):
                    break
                else:
                    print('Usuario inexistente.')
        
    try:
        with open(f'{path_users}/{user}.txt','rt',encoding='UTF-8') as datos:
            nombre, pw_account = datos.readline().split(';')
            while True:
                try: 
                    pw_input = input('Ingrese la contraseña (-1 para salir): ')
                except (KeyboardInterrupt, EOFError):
                    print('')
                    quit()
                except Exception as e: 
                    print('Ocurrió un error inesperado.')
                else: 
                    if pw_input == '-1':
                        return False
                    else:
                        if pw_input != pw_account: 
                            intentos += 1
                            print(f'Contraseña errónea {intentos}/3')
                        else: 
                            return nombre 
            
                        if intentos == 3: 
                            return False 
                    
    except Exception as e:
        print(f'Ha ocurrido un error: {e}')

    return 