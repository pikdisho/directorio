# Coloque el módulo del ejercicio anterior dentro de un paquete. En un
# módulo que esté fuera de ese paquete, cree una función de suma de
# decimales que redondee el resultado haciendo uso de la función
# redondear() del paquete recién creado

from funciones_posiblemente_utiles import redondear

def sumadenumerosdecimales():
    numerodecimal1 = float(input('Introduzca el primer numero decimal a sumar: '))
    numerodecimal2 = float(input('Introduzca el segundo numero decimal a sumar: '))
    sumadecimal = redondear(numerodecimal1+numerodecimal2)
    print('→ El resultado de la suma redondeada es:', sumadecimal)

# sumadenumerosdecimales()

# Usando el módulo datetime, escribe un programa que muestre la fecha
# y hora actuales del sistema.

from datetime import date, time, datetime

def fecha():
    datosfecha = datetime.now()
    print('→', datosfecha.strftime('Hoy es %A %d de %B de %Y. La hora actual del sistema es %H:%M:%S.'))

# → Fuente: https://aprendeconalf.es/docencia/python/manual/datetime/

# Escriba un programa que devuelva un número par al azar entre 2 y 10
# (pista: para comprobar si se pueden generar todos los números, pruebe
# ejecutar el programa dentro de un ciclo infinito).

import os
import random
import time

def funcionaleatoriopar():
    while True:
        numeroaleatorio = random.randint(1,10)   
        if (numeroaleatorio%2 == 0):
            return(numeroaleatorio)
        else:
            numeroaleatorio = random.randint(1,10)

def aleatoriopar():
    mensaje = 'Generando numero aleatorio par'

    for i in range (0,4):
        os.system('cls')
        print(mensaje)
        mensaje += '.'
        time.sleep(1)
    
    print('→ Ha salido el', funcionaleatoriopar())

# 5. Bola mágica: La bola mágica (Magic 8 ball) es un popular juguete usado
# para la adivinación o para buscar consejo. Su mecanismo es muy simple:
# ante una pregunta del usuario, la bola responde con una de 8 posibles
# respuestas:
# - Es seguro que sí
# - Las chances son buenas
# - Puedes contar con ello
# - Pregúntame de nuevo más tarde
# - Concéntrate y pregunta de nuevo
# - No veo con claridad, intenta de nuevo
# - Mi respuesta es no
# - Mis fuentes me dicen que no
# Escriba una función en Python para simular la bola mágica.

def bolamagica():

    os.system('cls')
    repetir = ''
    while (repetir.lower != 'n'):
        print('→ BIENVENIDO A LA BOLA MAGICA ←')

        lista_de_respuestas = ['Es seguro que sí', 'Las chances son buenas', 'Puedes contar con ello', 'Pregúntame de nuevo más tarde', 'Concéntrate y pregunta de nuevo', 'No veo con claridad, intenta de nuevo', 'Mi respuesta es no', 'Mis fuentes me dicen que no']

        print('Escribe tu pregunta... ')
        input('→ ')

        print(lista_de_respuestas[random.randint(0,7)])

        repetir = (input('→ Desea jugar otra vez? (Y/N): '))

    print('La bola magica se despide.')
    time.sleep(1)      

bolamagica()

