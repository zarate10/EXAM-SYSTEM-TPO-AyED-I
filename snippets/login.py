# -*- coding: utf-8 -*-
#
#  login.py
#  
#  Trabajo Práctico Final
#  Algoritmos y Estructuras de Datos I
#  Equipo: Cañete Andrés, Ciardelli Martín, Touris Santiago, Traba Federico, Zarate Lautaro

import os
from snippets.registro import usuario_existe

path_users = './db/usuarios'
usuarios = os.scandir(path_users)

def login():
    intentos = 0
    user = input('Ingrese el usuario: ')
    if usuario_existe(user):
        user += '.txt'
        for usuario in usuarios:
            if usuario.name == user:
                try:
                    with open(f'{path_users}/{user}','r',encoding='UTF-8') as datos:
                        nombre,contraseña = datos.readline().split(';')
                        while True:
                            if intentos == 3:
                                #No se va a mostrar en el main (?)
                                print('CANTIDAD DE ERRORES EXCEDIDA')
                                return False
                            elif intentos == 2:
                                print('ÚLTIMO INTENTO')
                            password = input('Ingrese la contraseña: ')
                            if password == contraseña:
                                return True
                            else:
                                intentos += 1 
                    
                except Exception as e:
                    print(f'Ha ocurrido un error: {e}')
    else:
        print('USUARIO INEXISTENTE')
        return False