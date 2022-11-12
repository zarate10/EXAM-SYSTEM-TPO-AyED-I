# -*- coding: utf-8 -*-
#
#  registro.py
#  
#  Copyright 2022 by Diógenes y los perros
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
            print('El usuario existe o es incorrecto.')
        else:
            return new_user


def registrar(user): 

    password = ''
    
    try: 
        
        with open(f'{path_users}/{user}.txt', 'wt', encoding='UTF-8') as fuser:

            while True:
                password = input('Ingrese password: ')

                if ';' in password:
                    print('Error, el usuario no debe contener ";"')
                else: 
                    break 
            
            fuser.write(f'{user};{password}')

    except Exception as e: 
        print('Ocurrió un error:', e)

    return 
