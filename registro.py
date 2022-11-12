# -*- coding: utf-8 -*-
#
#  registro.py
#  
#  Copyright 2022 by Diógenes y los perros
#  Equipo: Cañete Andrés, Ciardelli Martín, Touris Santiago, Traba Federico, Zarate Lautaro

import os 

usuarios = os.scandir('./db/usuarios')

def usuario_existe(new_user): 
    new_user += '.txt'

    for user in usuarios: 
        
        if user.name == new_user: 
            return True 

    return False

