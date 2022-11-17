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
  return year % 4 == 0 and year % 100 != 0 or year % 400 == 0

def reset(dia,mes,anio):
  dia = 1
  if mes != 12:
    mes += 1
  else:
    mes = 1
    anio +=1
  
  return dia,mes,anio

def comprobacion(dia,mes,anio):
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
  #Funcion para calcular total de dias entre 2 fechas
  contador = 0
  while (str(dia1)+str(mes1)+str(anio1)) != (str(dia2)+str(mes2)+str(anio2)):
    dia1 += 1
    dia1,mes1,anio1 = comprobacion(dia1,mes1,anio1)
    contador +=1

  return contador

def es_menor(fecha='20221211'):
    #Esta funcion verifica que la fecha pasada como parametro, (la del examen) sea una fecha del FUTURO y no haya pasado
    hoy = dt.date.today()
    fecha = dt.date(int(fecha[:4]),int(fecha[4:6]),int(fecha[6:]))
    return not hoy < fecha

#A DIAS RESTANTES HAY QUE PASARLE UNA FECHA EN FORMATO AAAAMMDD // EN FORMATO STRING
def dias_restantes(fecha):
    today = dt.date.today()
    dias = diasEntre(today.day,today.month,today.year,int(fecha[6:]),int(fecha[4:6]),int(fecha[:4]))

    return dias
