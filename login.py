import os
from registro import * 

usuarios = os.scandir('./db/usuarios')

def login():
    intentos = 0
    user = input('Ingrese el usuario: ')
    if usuario_existe(user):
        user += '.txt'
        for usuario in usuarios:
            print(usuario)
            if usuario == user:
                print('ENCONTRADO')
                while intentos < 4:
                        password = input('Ingrese la contraseña: ')
    else:
        print('USUARIO INEXISTENTE')
        return False


login()