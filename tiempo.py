import time
import datetime as dt
#TIENE QUE LLEGAR UNA FECHA MAS GRANDE QUE LA DEL DIA DE HOY

TREINTA = [4,6,9,11]
TREINTIUNO = [1,3,5,7,8,10,12]

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
  if mes in TREINTA and dia>30:
      dia,mes,anio = reset(dia,mes,anio)
      
  elif mes in TREINTIUNO and dia>31:
    dia,mes,anio = reset(dia,mes,anio)
      
  elif mes == 2:
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

#A DIAS RESTANTES HAY QUE PASARLE UNA FECHA EN FORMATO AAAAMMDD
def dias_restantes(fecha):
    today = dt.date.today()
    dias = diasEntre(today.day,today.month,today.year,int(fecha[6:]),int(fecha[4:6]),int(fecha[:4]))

    return dias


