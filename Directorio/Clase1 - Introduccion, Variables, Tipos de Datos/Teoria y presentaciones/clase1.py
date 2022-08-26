#Curso Python - Clase 1

##Comentarios
#Los usamos para descibrir algo a las personas que lean nuestro codigo, la maquina los ignora al ejecutar el programa
#Esto es un comentario de una linea (signo numeral)
'''
esto es
un comentario
de multiples lineas (tres comillas simples o dobles al comienzo y al final del comentario (ambas deben ser del mismo tipo)
'''

##Variables
#Asignacion de variables: asociamos un valor con un nombre para identificarlo

var1 = 3 #entero
var2 = 3.0 #float
var3 = "hola mundo" #string
var4 = True #booleano (notese la T en mayusculas)

#En el primer ejemplo, asignamos el valor entero 3 al nombre var1, para mostrar el valor de una variable en pantalla usamos la funcion print()
#Como este archivo tiene muchos print(), para no mostrar todo de una vez y confundir al lector, muchas lineas estan comentadas para que no se ejecuten, puede quitarles el comentario borrando el numeral o las tres comillas

#print(var1)

#Podemos cambiar el valor al que hace referencia un nombre, sin importar el tipo de dato (entero, string, etc.), por eso decimos que es una 'variable'
'''
var1 = "nuevo valor" 
print(var1)
'''

##Operaciones entre valores
#Cada tipo de datos que viene con Python tiene sus propias operaciones permitidas

#Enteros
"""
var1 = 3 + 6
var2 = var1 * 3
var3 = 5+5*8
var4 = (21+2)*2

print(var1)
print(var2)
print(var3)
print(var4)
"""

#Flotantes
"""
mi_flotante = 3.0 * 2 #notese que una operacion entre un flotante y un entero devuelve un flotante
mi_flotante2 = 3.0 + 2.5
print(mi_flotante)
print(mi_flotante2)
"""

#divisiones y restos
"""
mi_flotante3 = 3/2 #el operador de division siempre devuelve un flotante
mi_entero = 5//2 #el operador de division entera devuelve solo la parte entera de la division
mi_resto = 5%2 #el operador de modulo devuelve el resto de una division entera

print(mi_flotante3)
print(mi_entero)
print(mi_resto)
"""

#Strings
"""
cadena1 = "hola"
cadena2 = 'mundo' #podemos usar comillas simples o dobles para declarar una string, siempre y cuando terminemos con la misma con la que empezamos
cadena_suma = cadena1 + ' ' + cadena2
print(cadena_suma)
"""

#nota: tambien podemos imprimir directamente el resultado de una expresion, no es necesario asignar primero una variable
# y luego imprimirla, aunque es conveniente si queremos seguir trabajando con ese resultado
#print(cadena1 + ' ' + cadena2)

# #Obtener el tipo de un dato
# mi_variable = True
# print(type(mi_variable))
# print(type("hola"))
# print(type(12))
# print(type(12.0))
# mi_variable = "True"
# print(type(mi_variable))

#Operadores logicos
#nos devuelven un valor verdadero o falso (booleano)

#operador de igualdad, dos signos = (comparelo con el de asignacion, un solo signo =)
"""
son_iguales = '3' == 3
print(son_iguales) 
print(3 == 3)
"""

#operador de desigualdad, !=
"""
print(3 != 'holu')
print(3 != 3)
"""

#comparadores
"""
print(3<2)
print(3>=3)
print(3<=5)
"""

##Input del usuario y Convertir entre tipos de datos
#La funcion input() viene incluida en Python 3 para permitir que el usuario ingrese un valor
#podemos pasarle a la funcion un mensaje para el usuario que va entre parentesis. Esto es lo que se llama un parametro, mas sobre eso en la proxima clase!
#Con esta funcion, lo que el usuario ingrese siempre es intrepretado como una string
"""
entrada = input("Por favor ingrese un valor: ")
print("usted ingreso: " + entrada)
"""

#Para convertir un tipo de datos a otro, usamos funciones que tienen el mismo nombre que el tipo de datos que buscamos: int(), float(), str(), bool()
"""
print(int(4.6))
print(int("4"))
print(float("6.7"))
print(float(5))
print(str(42) + " es el secreto del universo")
print(bool("True"))
"""
"""
numero_en_str = input("Ingrese un numero: ")
print(int(numero_en_str) + 5)
"""




