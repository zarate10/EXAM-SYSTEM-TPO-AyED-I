# -*- coding: utf-8 -*-
#
#  registro.py
#  
#  Trabajo Práctico Final
#  Algoritmos y Estructuras de Datos I
#  Equipo: Cañete Andrés, Ciardelli Martín, Touris Santiago, Traba Federico, Zarate Lautaro

import os 
from os import path 

path_users = './db/usuarios'
path_fechas  = './db/fechas'
usuarios = os.scandir(path_users)

def usuario_existe(new_user, path): 
    """
    Función para validar si el txt asignado al usuario que se busca existe.

    Args:
        - new_user: nombre del nuevo usuario tipo string.
        - path: ruta de los usuarios para comprobar si existe.
    return:
        - verdadero si existe y falso si no existe.
    """
    if os.path.isfile(f'{path}/{new_user}.txt'):
        return True 
    
    return False

def validar_username():
    """
    Valida que la composición del username cumpla con los requisitos correspondientes.
    En caso de que cumpla con todos los requisitos, comprueba si el usuario existe.
    Si el usuario no está registrado y cumple con los requisitos de validación, retorna el nuevo usuario.
    """
    while True: 
        new_user = input('\nIngrese un nuevo usuario: ')
        if not new_user.isalnum(): 
            print('Nombre de usuario debe contener sólo letras y números.')
        elif len(new_user) < 3: 
            print('El nombre de usuario debe ser mayor a tres caracteres.')
        elif usuario_existe(new_user, path_users): 
            print('El nombre de usuario ya existe')
        else: 
            if not usuario_existe(new_user, path_users): 
                return new_user.strip()

def crear_password():
    """
    Le pide a un usuario una nueva contraseña, a su vez valida su longitud y que no contenga ";".
    En caso de que cumpla con los susodichos requisitos, devuelve la nueva password. 
    """
    while True:
        password = input('Ingrese password: ')

        if ';' in password: 
            print('Error, el usuario no debe contener ";"')
        elif len(password) < 5:
            print('La contraseña debe tener más de cinco caracteres.') 
        else: 
            return password

def registrar(): 
    """
    Graba al nuevo usuario en caso de que todos los datos sean correctos, 
    en el path especificado de forma global. 
    """
    user = validar_username()

    if user: 
        pw = crear_password()

        try: 
            
            with open(f'{path_users}/{user}.txt', 'wt', encoding='UTF-8') as fuser:                
                fuser.write(f'{user};{pw}')

            with open(f'{path_fechas}/{user}_fechas.txt', 'wt', encoding='UTF-8') as filefecha:
                pass

        except Exception as e: 
            print('Ocurrió un error:', e)

    return 