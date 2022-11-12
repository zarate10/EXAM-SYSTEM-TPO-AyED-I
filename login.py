import os
from registro import * 
path_users = './db/usuarios'
usuarios = os.scandir(path_users)

def login():
    intentos = 0
    user = input('Ingrese el usuario: ')
    if usuario_existe(user):
        user += '.txt'
        for usuario in usuarios:
            if usuario.name == user:
                with open(f'{path_users}/{user}','r',encoding='UTF-8') as datos:
                    nombre,contraseña = datos.readline().split(';')
                    while True:
                        if intentos == 4:
                            print('CANTIDAD DE ERRORES EXCEDIDA')
                            return False
                        password = input('Ingrese la contraseña: ')
                        if password == contraseña:
                            return True
                        else:
                            intentos += 1 
    else:
        print('USUARIO INEXISTENTE')
        return False

print(login())