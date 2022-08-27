import time
time.sleep(1)
'''
 1. Pida un número al usuario y determine si es par o impar.
 '''

# print("Ejercicio 1")
# time.sleep(2)

# numpunto1 = int(input('Bienvenido, ingrese el numero a determinar si es par o no: '))

# if numpunto1%2 == 0:
#     print('El numero introducido es par')
# else:
#     print('El numero introducido es impar')

# time.sleep(2)

#--------------------------------------------------------------

'''
2. Escriba una cadena if-elif-else que determine el estado de vida de una
persona.
• Si la persona tiene menos de 2 años, muestre un mensaje que diga que
es un bebe.
• Si tiene al menos 2 años, pero menos de 4, muestre que es un infante.
• Si tiene al menos 4, pero menos de 12, muestre que es un niño.
• Si tiene al menos 13, pero menos de 20, muestre que es un adolescente.
• Si tiene al menos 20 pero menos de 65, muestre que es un adulto.
• Si tiene 65 o más, muestre que es un anciano.
'''

# print("Ejercicio 2")
# time.sleep(2)

# edadpunto2 = int(input('Para determinar el estado de vida de la persona introduzca su edad: '))

# if edadpunto2<2:
#     print('La persona es un bebe')
# elif edadpunto2>=2 and edadpunto2<4:
#     print('La persona es un infante')
# elif edadpunto2>=4 and edadpunto2<12:
#     print('La persona es un niño')
# elif edadpunto2>=12 and edadpunto2<20:
#     print('La persona es un adolescente')
# elif edadpunto2>=20 and edadpunto2<65:
#     print('La persona es un adulto')
# elif edadpunto2>65:
#     print('La persona es un anciano')
# else:
#     print('La edad introducida no es valida')

time.sleep(1)

'''3. Infinito: Cree un ciclo que nunca termine y ejecútelo. Puede probarlo
haciendo que muestre algo en pantalla por cada pasada del ciclo. Para
finalizarlo, presione Ctrl-C o el comando para detener la ejecución
correspondiente a su edito'''

# print("Ejercicio 3")
# time.sleep(2)

# condicioninfinita = True
# while condicioninfinita == True:
#     print('Este loop es infinito, no se detiene (o si?)')

# time.sleep(1)

'''4. Escriba un programa que contenga dos ciclos while anidados que
muestre los enteros del 1 al 100, diez números por línea, como se muestra
abajo'''

# print("Ejercicio 4")
# time.sleep(2)

# limitepunto4 = 0
# contadorpunto4 = 0
# escribirpunto4 = 1
# lineapunto4 = ' '

# while limitepunto4 < 10:
#         while contadorpunto4 < 10:
#             lineapunto4 += ' ' + str(escribirpunto4)
#             escribirpunto4 +=1
#             contadorpunto4 +=1
#         print(lineapunto4)
#         contadorpunto4 = 0
#         lineapunto4 = ' '
#         limitepunto4 +=1
#         time.sleep(1)

'''5. Resuelva el ejercicio anterior usando solo un ciclo while'''

# print("Ejercicio 5")
# time.sleep(2)

# limitepunto5 = 0
# numeros = 1
# lineapunto5 = ' '

# while limitepunto5 < 10:
#     for i in range (10):
#         lineapunto5 += ' ' + str(numeros)
#         numeros +=1
#     print(lineapunto5)
#     lineapunto5 = ' '
#     limitepunto5+=1
#     time.sleep(1)

'''6. Escriba una función que muestre todos los números primos entre 1 y un
número n que es ingresado por parámetro.'''

print("Ejercicio 6")
time.sleep(2)
def numerosprimos(numpunto6):

    numpunto6 = int(input('Ingrese el numero maximo a calcular si es primo o no'))

    for divisor in range (1, numpunto6):
        print('a')

numerosprimos(input(numpunto6))

