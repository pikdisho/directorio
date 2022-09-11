# Coloque el módulo del ejercicio anterior dentro de un paquete. En un
# módulo que esté fuera de ese paquete, cree una función de suma de
# decimales que redondee el resultado haciendo uso de la función
# redondear() del paquete recién creado

from funciones_posiblemente_utiles import redondear

def sumadenumerosdecimales():
    numerodecimal1 = float(input('Introduzca el primer numero decimal a sumar: '))
    numerodecimal2 = float(input('Introduzca el segundo numero decimal a sumar: '))
    sumadecimal = round(numerodecimal1+numerodecimal2)
    print('→ El resultado de la suma redondeada es:', sumadecimal)

# sumadenumerosdecimales()

# # Usando el módulo datetime, escribe un programa que muestre la fecha
# # y hora actuales del sistema.

# import datetime

