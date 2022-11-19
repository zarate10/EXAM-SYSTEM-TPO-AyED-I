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
    #Función para validar si el txt asignado al usuario que se busca existe o no
    if os.path.isfile(f'{path}/{new_user}.txt'):
        return True 
    
    return False

def validar_username():
    #Valida tanto la composición del username
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
    #Valida su longitud y que no tenga ";" que afecte el split del txt
    while True:
        password = input('Ingrese password: ')

        if ';' in password: 
            print('Error, el usuario no debe contener ";"')
        elif len(password) < 5:
            print('La contraseña debe tener más de cinco caracteres.') 
        else: 
            return password

def registrar(): 
    #Registra usuario y contraseña en su txt único
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