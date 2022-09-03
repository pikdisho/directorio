##Curso Python - Clase 4
##Modulos y Paquetes
"""
Llamamos modulo a un solo archivo .py, que puede contener definiciones de funciones, variables, clases (todavia no vimos esto), incluso codigo que esta en el cuerpo principal y se ejecuta cada vez que importamos o ejecutamos el modulo
Para importar un modulo, o una parte de este, dentro de otro usamos la palabra reservada import de esta forma:

import modulox

Para llamar una funcion, variable u otra definicion desde el modulo importado tengo que colocar el nombre del modulo seguido por un punto. Por ej, si modulox tiene una funcion saludar() debo invocarla como:

modulox.saludar()

Tambien puedo importar partes del modulo que necesito sin tener que importar todo, esto puedo hacerlo como sigue:

from modulox import saludar

o tambien:

import modulox.saludar

En el ultimo caso debo llamar la funcion igual que antes, pero cuando uso from solo tengo que escribir el nombre que este a la derecha del import:

saludar()

Los import y los from se suelen colocar al principio del archivo de codigo, si bien no es necesario esta es una convencion MUY establecida, por lo que casi es una regla.

En el siguiente ejemplo, suponemos un modulo llamado mi_modulo.py que tiene definida una funcion para sumar dos numeros.
"""
#import mi_modulo
#from mi_modulo import suma

#print(mi_modulo.suma(2,3))
#print(suma(10,2))

"""
LLamamos paquete a una carpeta que contiene mas de un modulo, e incluso otros paquetes.
Son utilizados para agrupar modulos que tengan relacion entre si, por ejemplo si tenemos los modulos trigonometria.py, aritmetica.py, analisis.py podemos agruparlos en un paquete (carpeta) Calculadora.
Al igual que los elementos dentro de un modulo, para hacer referencia a un modulo dentro de un paquete usamos un punto:

from paquete import modulo1
import paquete.modulo1
"""
#from paquete1.subpaq1.mi_modulo import suma
#from paquete1.subpaq1 import mi_modulo

#print(mi_modulo.suma(2,3))
#print(suma(10,2))
"""
Los modulos/paquetes que importemos deben estar en la misma carpeta que nuestro archivo actual para que la importacion funcione (a menos que sean paquetes de la libreria estandar, que es el siguiente tema)
Existe una manera de hacer que podamos importar paquetes que esten en otra carpeta del sistema, pero por cuestiones de tiempo lo dejamos como ejercicio para el lector
"""

##Librerias
"""
Una libreria es un conjunto de modulos/paquetes diseñado para contener funciones que pueden ser reusadas en diferentes proyectos y no tener que volver a escribirlas. Son colecciones de herramientas de programacion, como funciones y clases.
El conjunto de funciones y paquetes que viene incluido con cualquier instalacion de Python se conoce como la Libreria Estandar del lenguaje.

Por ejemplo, el modulo math contiene operaciones matematicas avanzadas como trigonometria, el modulo random contiene funciones que devuelven numeros aleatorios o elementos al azar de una secuencia, datetime contiene funciones para el manejo de fechas y horas, entre muchas otras.

Documentacion oficial de Python, incluyendo la liberia estandar y todos los detalles de cada modulo: https://docs.python.org/3/
"""
#import math
#import random
#import datetime

#Note como podemos importar modulos de la libreria estandar sin que estos archivos esten en la misma carpeta

#print(math.ceil(3.4)) #Ceil = Techo, nos devuelve el entero superior de un numero flotante
#print(math.floor(3.4)) #Floor = Piso, nos devuelve el entero inferior de un numero flotante
#print(math.fabs(-4)) #nos devuelve el valor absoluto como un float

#print(random.randint(1,5)) #Nos devuelve un entero al azar entre 1 y 5 (En este caso, el 5 no es exclusivo y tambien se incluye en la secuencia)
#print(random.choice(['elemento1', 'elemento2'])) #Nos devuelve un elemento al azar de la secuencia (lista)
#print(random.sample([1,2,3,4,5,6,7,8,9,10],3)) #Nos devuelve una muestra de 3 elementos de la lista de numeros

#hoy = datetime.datetime.today() #nos devuelve la fecha y hora actuales del sistema
#print(hoy) 
#print(hoy.day,hoy.month,hoy.year,hoy.hour,hoy.minute)
#print((hoy - datetime.datetime(1994,4,12))) #Con este modulo podemos operar sobre fechas, por ejemplo restando dos tipos de datos datetime obtenemos la cantidad de dias que tienen de diferencia


