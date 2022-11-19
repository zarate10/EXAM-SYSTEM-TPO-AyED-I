# -*- coding: utf-8 -*-
#
#  fechas.py
#  
#  Trabajo Práctico Final
#  Algoritmos y Estructuras de Datos I
#  Equipo: Cañete Andrés, Ciardelli Martín, Touris Santiago, Traba Federico, Zarate Lautaro

import os 
import datetime 

path_fechas  = './db/fechas'
from snippets.tiempo import es_menor, dias_restantes

def obtener_id(username): 
    """Se obtiene la última ID del archivo de fechas del usuario"""

    ultimo_id = 0 # acá guardamos la última ID encontrada

    try: 
        with open(f'{path_fechas}/{username}_fechas.txt', 'rt', encoding="UTF-8") as f_fechas: 

            for linea in f_fechas: 
                ultimo_id = linea.strip().split(";")

    except Exception as e: 
        print('Ocurrió un error:', e)

    return int(ultimo_id[0])


def obtener_fecha_examen(): 
    while True: 
        #id,fecha,materia,descripcion
        dia, mes, anio = input('Ingrese fecha (dd-mm-aaaa): ').split('-')
                
        if not es_menor(anio + mes + dia): 
            return dia, mes, anio 
        
def verificacion_in():
    while True:
        anio = input(f'Ingrese fecha (dd-mm-aaaa): ')
        if len(anio) >= 8:
            print(f'Ingrese con este formato: (dd-mm-aaaa)')
        break
    while True:
        materia = input(f'Ingrese materia: ')
        if agregar_materia(materia):
            break
        print(f'"Materia" debe contener como maximo 30 caracteres - Vuelva a intentarlo')
    while True:
        instancia = input(f'Ingrese instancia: ')
        if agregar_instancia(instancia):
            break
        print(f'"Instancia" debe contener como maximo 15 caracteres - Vuelva a intentarlo')
    return anio,materia,instancia

def agregar_fecha(username):
    
    id = 0

    if os.stat(f'{path_fechas}/{username}_fechas.txt').st_size != 0:
        id = obtener_id(username) + 1

    try: 
        with open(f'{path_fechas}/{username}_fechas.txt', 'at', encoding='UTF-8') as fechas: 

            # hacer verifcacion
            anio,materia,instancia = verificacion_in()

            dia, mes, anio = obtener_fecha_examen()

            if not id: 
                fechas.write(f'{id};{dia}-{mes}-{anio};{materia};{instancia}\n')
                return 

            fechas.write(f'{id};{dia}-{mes}-{anio};{materia};{instancia}\n')

    except Exception as e:
        print('Ocurrió un error:', e)

    return

def matriz_fechas(username):
    #Retorna la matriz con la fechas del usuario
    try:
        with open(f'{path_fechas}/{username}_fechas.txt', 'rt', encoding='UTF-8') as fechas:
            matriz = [linea.rstrip().split(';') for linea in fechas]
            
    except Exception as e:
        print('Ocurrió un error:', e)

    return matriz



def mostrar_fechas(matriz):
    #Muestra la matriz de la funcion matriz_fechas
    print('{:<2} | {:<10} | {:<15} | {:<20} | {:<15}'.format('ID','Fecha', "Días restantes", 'Materia', 'Instancia'))
    print('-'*85)
    for elem in matriz:
        print('{:<2} | {:<10} | {:<15} | {:<20} | {:<15}'.format(elem[0], elem[1], dias_restantes(''.join(elem[1].split('-')[::-1])), elem[2], elem[3]))
        
    return 

def id_fecha(matriz):
    while True: 
        try:
            id = int(input('Ingresar ID: '))
            matriz[id] 
        except IndexError: 
            print('No existe la ID seleccionada.')
        except Exception as e: 
            print('Error: ', e)
        else: 
            return id 
        
def agregar_materia(materia):
    return len(materia) > 0 and len(materia) < 31 and not ';' in materia

def agregar_instancia(instancia):
    return len(instancia) > 0 and len(instancia) < 16 and not ';' in instancia


def modificar_fechas(id, matriz, username):
    #Verificacion de los cambios del usuario
    anio,materia,instancia = verificacion_in()

    matriz[id] = [str(id), anio, materia, instancia] #Cambiamos la linea que desea modificar el usuario

    #Sacamos los datos del archivo e ingresamos la matriz con las actualizaciones del usuario
    try: 
        with open(f'{path_fechas}/{username}_fechas.txt', 'wt', encoding='UTF-8') as fechas:
            [fechas.write(f'{arr[0]};{arr[1]};{arr[2]};{arr[3]}\n') for arr in matriz]
    except Exception as e:
        print('Ocurrió un error:', e) 
    else: 
        pass

def eliminar_fechas(id,matriz,username):
    matriz.pop(id)

    for i in range(len(matriz)):
        matriz[i][0] = str(i)

    try: 
        with open(f'{path_fechas}/{username}_fechas.txt', 'wt', encoding='UTF-8') as fechas:
            [fechas.write(f'{arr[0]};{arr[1]};{arr[2]};{arr[3]}\n') for arr in matriz]
    except Exception as e:
        print('Ocurrió un error:', e) 

    else: 
        pass 

