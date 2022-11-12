# -*- coding: utf-8 -*-
#
#  registro.py
#  
#  Trabajo Práctico Final
#  Algoritmos y Estructuras de Datos I
#  Equipo: Cañete Andrés, Ciardelli Martín, Touris Santiago, Traba Federico, Zarate Lautaro

import os 

path_users = './db/usuarios'
usuarios = os.scandir(path_users)

def usuario_existe(new_user): 
    new_user += '.txt'

    for user in usuarios: 
        if user.name == new_user: 
            return True 

    return False


# ERROR, si colocamos dos veces un nombre utilizado lo admite
def crear_usuario():

    while True:
        new_user = input('Ingrese un nuevo usuario: ')
        
        if usuario_existe(new_user): 
            print('Usuario existente.')
            return False
        else: 
            return new_user

def crear_password():

    while True:
        password = input('Ingrese password: ')

        if ';' in password: 
            print('Error, el usuario no debe contener ";"')
        elif len(password) < 5:
            print('La contraseña debe tener más de cinco caracteres.') 
        else: 
            return password


def registrar(): 

    user = crear_usuario()

    if user: 
        pw = crear_password()

        try: 
            
            with open(f'{path_users}/{user}.txt', 'wt', encoding='UTF-8') as fuser:
                
                fuser.write(f'{user};{pw}')

        except Exception as e: 
            print('Ocurrió un error:', e)

    return 

