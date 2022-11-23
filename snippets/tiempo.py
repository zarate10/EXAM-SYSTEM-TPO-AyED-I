# -*- coding: utf-8 -*-
#
#  tiempo.py
#  
#  Trabajo Práctico Final
#  Algoritmos y Estructuras de Datos I
#  Equipo: Cañete Andrés, Ciardelli Martín, Touris Santiago, Traba Federico, Zarate Lautaro

import time
import datetime as dt

#TIENE QUE LLEGAR UNA FECHA MAS GRANDE QUE LA DEL DIA DE HOY

LIMITES = (31,28,31,30,31,30,31,31,30,31,30,31)

def validarBisiesto(year):
  """
  Recibe un entero que indica el año y verifica si corresponde a un año bisiesto.
  
  Args:
  Recibe como parametro un entero correspondiente al año ingresado por el usuario.

  La funcion debe retornar True si el año es bisiesto, de lo contrario, retorna False.
  """
  return year % 4 == 0 and year % 100 != 0 or year % 400 == 0

def reset(dia,mes,anio):
  """Recibe como parametro tres enteros, si el dia supera la cantidad de dias de un mes 
  y el mes es distinto de 12, le suma uno al mes y resetea el dia a 1.
  Si llegase al limite (12) resetea el dia a 1, el mes tambien y le suma uno al año.
  
  Recibe tres enteros

  Debera retornar el mes actualizado o el mes y año actualizados.
  """
  #Incrementar por mes recorrido

  dia = 1
  if mes != 12:
    mes += 1
  else:
    mes = 1
    anio +=1
  
  return dia,mes,anio

def comprobacion(dia,mes,anio):
  """Esta funcion recibe tres enteros (dia/mes/año) la cual comprobara la cantidad de dias disponibles en el mes ingresado
  y definira sus limites. Tambien hara uso de las funciones ValidarBisiesto y Reset, la cual se encargaran de marcar
  los limites de cada mes.

  La funcion recibira tres enteros

  Devolvera la fecha actualizada en caso de haber superado algun limite.
  """
  if mes != 2:
      if dia > LIMITES[mes - 1]:
        dia,mes,anio = reset(dia,mes,anio)
  else:
      if validarBisiesto(anio) and dia == 30:
        dia,mes,anio = reset(dia,mes,anio)

      elif not validarBisiesto(anio) and dia == 29:
        dia,mes,anio = reset(dia,mes,anio)

  return dia,mes,anio

def diasEntre(dia1,mes1,anio1,dia2,mes2,anio2):
  """La funcion recibira 6 enteros correspondientes a una fecha base y otra fecha de la cual queremos calcular
  la cantidad de dias que hay entre ambas fechas
  
  Debe recibir 6 enteros para luego castearlos a string y realizar los calculos
  
  Retornara un contador que indicara la cantidad de dias entre ambas fechas."""
  #Funcion para calcular total de dias entre 2 fechas
  contador = 0
  while (str(dia1)+str(mes1)+str(anio1)) != (str(dia2)+str(mes2)+str(anio2)):
    dia1 += 1
    dia1,mes1,anio1 = comprobacion(dia1,mes1,anio1)
    contador +=1

  return contador

def es_menor(fecha='20221211'):

    """Esta funcion verifica que la fecha pasada como parametro, (la del examen) sea una fecha del FUTURO 
    y no haya pasado.
    
    Recibe un string que indica la fecha (ddmmaaaa)
    
    Devuelve True si la fecha es del futuro, de lo contrario, devuelve False"""
    hoy = dt.date.today()
    fecha = dt.date(int(fecha[:4]),int(fecha[4:6]),int(fecha[6:]))
    return not hoy < fecha

#A DIAS RESTANTES HAY QUE PASARLE UNA FECHA EN FORMATO AAAAMMDD // EN FORMATO STRING
def dias_restantes(fecha):
    """
    Esta funcion recibe un string correspondiente a una fecha y llama a diasEntre para calcular la cantidad de dias
    entre fechas.

    Recibe un string correspondiente a una fecha

    Devuelve la cantidad de dias restantes para llegar a la fecha
    """
    today = dt.date.today()
    dias = diasEntre(today.day,today.month,today.year,int(fecha[6:]),int(fecha[4:6]),int(fecha[:4]))

    return dias