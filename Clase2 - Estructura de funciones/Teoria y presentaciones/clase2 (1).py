##Curso Python - Clase 2
##Estructuras de control y funciones

##Estructura selectiva: if-elif-else
#Las usamos para decidir sobre una (o varias) condicion logica -algo que se puede evaluar si es verdadero o falso- y decidir en base a esta que camino debe tomar nuestro programa
#Bloque de codigo: Una o varias lineas de codigo que se ejecutan debajo de alguna estructura de control
"""
if True:
    print("Hola a todos")
    print("Esta es la segunda linea del bloque")
    print("Esta es la tercera linea del bloque")
    
if False:
    print("Adios a todos")
"""
"""
if (3-4 == -1):
    print("Yo creo que si")

if 5 > 3.4:
    print("Yo creo que si")
"""
"""
if (2>1) and (3*2 == 6):
    print("Todas las clausulas se cumplen")

if (1>2) and (3*2 == 6):
    print("Todas las clausulas se cumplen")

if (1>2) or (3*2 == 6):
    print("Por lo menos una clausula se cumplio")

if not(2<1):
    print("Se cumple la condicion inversa")
"""

#Bloque alternativo: Solo se ejecuta si no se cumple la condicion del if (va sin condicion)
"""
if (4-3 == 1):
    print("Se cumplio la condicion")
else:
    print("No se cumplio")
"""
"""
c = 3
if (c-3 == 1):
    print("Se cumplio la condicion")
else:
    print("No se cumplio")
"""
#Multiples alternativas
"""
if (3-3 == 1):
    print("Se cumplio la primera condicion")
elif 3>2:
    print("Se cumple la alternativa")


if (3-3 == 1):
    print("Se cumplio la primera condicion")
elif 5>4:
    print("Se cumple la primera alternativa")
    print()
    print("entro por aca")
elif not(3==3):
    print("Se cumple la segunda alternativa")
else:
    print("No se cumplio ninguna condicion")
"""


##Estructura repetitiva condicional: Ciclo while
#Lo usamos para repetir un bloque de codigo hasta que se cumpla/deje de cumplirse una condicion logica
"""
var = 5
while var > 3:
    print ("valor de var: " + str(var))
    print("Todavia se cumple")
    var = var - 1

print("Terminaste")
"""

"""
var = 5   
mensaje = "buenas tardes"
while not(var < 3) and not(mensaje == "buenas tardes"):
    print("Todavia se cumple")
    var -= 1
    mensaje = "buenas noches"
"""
#Las palabras reservadas break y continue
#break sirve para salir del ciclo en el que estamos actualmente
#continue sirve para hacer que un ciclo vuelva al comienzo incluso si no llegamos al final del bloque
#Compare los dos siguientes codigos:
"""
var = 10
while var > 0:              
   var -= 1
   if var == 5:
      break #palabra reservada de Python para salir del ciclo actual
   print('Valor actual :', var)
print("Salimos del ciclo!")
"""
"""
var = 10
while var > 0:              
   var -= 1
   if var == 5:
      continue #palabra reservada de Python para volver al comienzo del ciclo
   print('Valor actual :', var)
print("Salimos del ciclo!")
"""
#Cuando la condicion nunca deja de cumplirse, entramos en un ciclo infinito
"""
while True:
    print("Ciclo infinito!")
"""
#Los ciclos infinitos pueden ser utiles. Por ejemplo, si queremos entrar a un ciclo repetitivo sin importar si la condicion se cumple o no yevaluar recien al final, de modo que se ejecute por lo menos una vez
"""
while True:
    print("Por lo menos una vez se va a mostrar este mensaje")
    if 6 > 2:
        break
""" 
#(Note como las estructuras de control se pueden combinar, colocando una dentro de otra)


##Estructura repetitiva no mcondicional: Ciclo for
#La usamos para repetir un bloque de codigo una cantidad determinada de veces o para recorrer los elementos en una secuencia (mas sobre secuencias en la proxima clase)
"""
x=5
for i in range(10):
    if x == i:
        print("Es el numero " + str(i))
    print("Pasada actual: ", i)
"""
#La funcion de Python range([comienzo], final, [paso]) nos devuelve una secuencia de numeros desde "comienzo" hasta "final"-1, devolviendo 1 cada "paso" numeros.
#Los argumentos entre corchetes son opcionales, por defecto comienza en 0 y va de a 1 numero.
"""
for i in range(2,10):
    print(i)

print()

for i in range(0,11,2):
    print(i)
"""
#break y continue tambien funcionan en los ciclos for
"""
for i in range(10):
    print("Iteracion numero", i)
    break


var = 10
for numero in range(1,7):              
   if numero == 5:
      continue
   print('Valor actual :', numero)
"""
#Ciclos anidados: Ciclos dentro de otros ciclos
'''
for i in range(10):
    for j in range(10):
        print(str(i) + str(j))
'''

##Funciones
#Una funcion es una pieza de codigo independiente capaz de realizar una tarea especifica, que normalmente toma una o mas entradas y devuelve una o mas salidas (a veces solo cumple su tarea sin pedir ni devolver nada)
#Las funciones son fundamentales para diseñar soluciones buenas que dividan un problema en problemas mas pequeños y manejables, y si ocurre un error sabemos a donde mirar!
"""
#Definicion de la funcion
def suma(numero1, numero2):
    resultado = numero1 + numero2
    return resultado

#Llamada a la funcion
mi_suma = suma(2,3)
print(mi_suma)
"""
#numero1 y numero2 son los PARAMETROS de la funcion: Las entradas que la funcion requiere para cumplir su tarea.
#Lo que esta despues de la palabra reservada return es la salida de la funcion, lo que esta devuelve. Se puede mostrar en pantalla con la funcion print(), se puede asignar a una variable, o cualquier otra operacion.
#Las funciones, lleven parametros o no, siempre se llaman con parentesis despues del nombre. Ejemplo: print() sin parametros imprime una linea en blanco

#No es necesario que una funcion tenga entradas y/o salidas
#En este caso, la funcion por defecto devuelve un valor None que se puede pensar como un elemento 'vacio' que es de su propio tipo. Podemos ignorar este hecho llamando a la funcion sin asignarle su salida a nada:
"""
def saludar():
    print("Hola mundo!")

saludar()
"""
#parametros por defecto: podemos pasar valores por defecto a uno o mas parametros de nuestras funciones para que las mismas no nos den problemas cuando las llamamos sin pasarles estos parametros
#los parametros por defecto SIEMPRE van despues de los que no son por defecto
"""
def saludo_personal(nombre, edad, mensaje="Que tengas un buen dia!"):
    print("Hola " + str(nombre) + "!")
    print("Tu edad es " + str(edad))
    print("Y tu mensaje del dia es: " + str(mensaje))

saludo_personal("Rodrigo", 23)
saludo_personal("Pablo", 25, "Me gusta Python!")
"""
#Funciones como print(), range(), int(), str() y otras vienen incluidas en Python, por eso no es necesario definirlas

##Metodos
#Son funciones que tienen una sintaxis especial, ya que se llaman sobre un tipo de dato particular y para ello se utiliza un punto entre el nombre de
#nuestro valor y el nombre del metodo en si. Por ejemplo, con las strings tenemos varios metodos, entre ellos:
#''.split()
'''
st = 'valor'
print(st.replace('a', 'e')) #Remplaza en la string de la variable st las letras 'a' por la letra 'e' (por defecto solo en la primera que encuentra, si queremos mas debemos pasarle un tercer parametro que sea la cantidad)

st = 'valora'
print(st.replace('a', 'e', -1)) #-1 reemplaza todas las ocurrencias de la string 'a' por 'e'

titulo = "la guerra de las galaxias"
print(titulo.title())

print('hola'.upper())
print('HOlA'.lower())
'''
#Para ver una descripcion resumida de cualquier metodo/funcion/tipo de dato/etc sobre el que coloquemos el cursor
#vamos a File>Settings>Editor>General y chequeamos la opcion "Show quick documentation on mouse move" bajo la categoria "Other"
#Si queremos la misma funcionalidad por defecto en todos los proyectos, en vez de Settings entramos en Default Settings.



