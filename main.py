from machine import ADC
from math import log
from time import sleep
termistor = ADC(26)
escalon = 3.3 / 65535

while(1):
  lectura = termistor.read_u16()
  tension = lectura * escalon #Multiplico el valor del ADC por cada escalon de la resolucion
  resistencia= (10000 / ((65535 / lectura)-1)) #Calculo de la resistencia del NTC
  temp= 3950 / (log(resistencia/10000)+(3950/298.15))-273.15
  print("El valor del ADC es: {}".format(lectura))
  print("El valor de tension medido es: {}".format(tension))
  print("El valor de resistencia del NTC es: {}".format(resistencia))
  print("La temperatura es: {:.2f}".format(temp))
  sleep(2)

