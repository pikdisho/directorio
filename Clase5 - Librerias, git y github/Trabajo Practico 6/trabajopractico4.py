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
    lista_de_respuestas = ['Es seguro que sí', 'Las chances son buenas', 'Puedes contar con ello', 'Pregúntame de nuevo más tarde', 'Concéntrate y pregunta de nuevo', 'No veo con claridad, intenta de nuevo', 'Mi respuesta es no', 'Mis fuentes me dicen que no']

    while (True):
        print('→ BIENVENIDO A LA BOLA MAGICA ←')

        print('Escribe tu pregunta... ')
        input('→ ')

        print(lista_de_respuestas[random.randint(0,7)])

        repetir = (input('→ Desea jugar otra vez? (Y/N): '))
        if (repetir=='n' or repetir=='N'): #if repetir.lower=='n': no funciona?
            break
        
    print('La bola magica se despide.')
    time.sleep(1)      

# bolamagica()

# 6. Encuentre el tiempo de ejecución de los programas de los ejercicios
# anteriores (pista: use el módulo time)



# 7. (Opcional) Sorteo: Escriba un programa que simule un sorteo donde
# toman uno o más papeles al azar de un pozo para elegir los ganadores.

def sorteo():
    os.system('cls')
    print('→ BIENVENIDO AL SORTEADOR ←')
    cantidad_ganadores = int(input('INGRESE LA CANTIDAD DE GANADORES: '))
    cantidad_numeros = int(input('INGRESE LA CANTIDAD DE NUMEROS VENDIDOS: '))

    for ganadores in range(1, cantidad_ganadores+1):
        print('→ El', str(ganadores)+'°', 'premio es para el numero', random.randint(0,cantidad_numeros))

# sorteo()
    
# 8. (Opcional) Escriba una función que pida al usuario ingresar su fecha de
# nacimiento y sea capaz de devolver la cantidad de días desde su
# nacimiento hasta hoy.

def diasdesdenacimiento():
    os.system('cls')
    fecha_actual = datetime.now()
    fecha_nacimiento=input('Ingrese su fecha de nacimiento(DD-MM-YYYY): ')
    
    anio=int(fecha_nacimiento[6:10])
    mes_nacimiento=int(fecha_nacimiento[3:5])
    dia_nacimiento=int(fecha_nacimiento[0:2])

    anio_actual = int(fecha_actual.strftime('%Y'))
    mes_actual = int(fecha_actual.strftime('%m'))
    dia_actual = int(fecha_actual.strftime('%d'))

    cantidad_de_dias_meses=[0,31,28,31,30,31,30,31,31,30,31,30,31]

    cantidad_anios_bisiestos = 0

    dias_anio_actual = 0
    dias_anio_nacimiento = 0
    dias_totales=0

    for aniorecorrido in range (anio+1, anio_actual-1):
        if aniorecorrido%4==0:
            cantidad_anios_bisiestos +=1
    
    for mesrecorrido in range (0,mes_actual):
        dias_anio_actual += cantidad_de_dias_meses[mesrecorrido]
    dias_anio_actual += dia_actual

    for mesrecorrido in range (mes_nacimiento,12+1):
        dias_anio_nacimiento += cantidad_de_dias_meses[mesrecorrido]
    dias_anio_nacimiento -= dia_nacimiento

    dias_totales = dias_anio_actual + dias_anio_nacimiento + 366*cantidad_anios_bisiestos + ((anio_actual-1) - anio - cantidad_anios_bisiestos)*365
   
    if (anio_actual%4==0):
        dias_totales+=1
    if (anio%4==0):
        dias_totales+=1

    
    print('Desde que naciste pasaron', dias_totales ,'dias')

diasdesdenacimiento()
