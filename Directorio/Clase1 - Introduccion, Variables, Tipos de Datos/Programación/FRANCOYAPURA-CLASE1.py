import time
'''
1. Mensaje simple: Almacene un mensaje en una variable e imprímalo en pantalla. Después cambie el valor del
mensaje e imprímalo nuevamente.
'''
print("Desarrollo Punto 1")
time.sleep(1)

mensaje = "Hola profe ¿Cómo anda la corrección?"
print (mensaje)
mensaje = "Hola profe ¿sigue ahí?"
print(mensaje)

time.sleep(4)

'''
2. Almacene el nombre de una persona en una variable, imprima un mensaje para esa persona. Por ejemplo “Hola
Fede, ¿te gustaría aprender a programar?”
'''
print("Desarrollo Punto 2")
time.sleep(1)

nombrepunto2 = "Messi"
print ( "Traeme la copa " + nombrepunto2 + " por favor te lo pido")

time.sleep(4)

'''
3. El número ocho: Escriba una suma, resta, multiplicación y división que resulten cada una en el número ocho.
Asegúrese de utilizar la función print() para ver los resultados en pantalla. Un ejemplo de línea es el siguiente:
print(5 + 3)
La salida debería mostrar el número ocho tantas veces como líneas haya escrito.
'''
print("Desarrollo Punto 3")
time.sleep(1)

print (4+4)
print (10-2)
print(4*2)
print (64/8)
print(2**3)
print(17//2)

time.sleep(4)

'''
4. Cree cuatro variables llamadas mi_entero, mi_decimal, mi_string y mi_booleano. Asigne a cada variable un valor del
tipo que le corresponda. Luego muestre en pantalla el tipo de cada variable usando la función type() combinando
todo con la función print() :
type(mi_entero)
type(mi_booleano)
La salida final debería contener las siguientes líneas (no importa el orden):
<class 'int'>
<class 'float'>
<class 'str'>
<class 'bool'>
'''
print("Desarrollo Punto 4")
time.sleep(1)

mi_entero = 21 
mi_decimal = 5.5
mi_string = "Messi"
mi_booleano = False 

print(type(mi_entero))
print(type(mi_decimal))
print(type(mi_string))
print(type(mi_booleano))

time.sleep(4)


'''
5. Escriba un programa que acepte un numero decimal como entrada y lo imprima sin lugares decimales.
'''
print("Desarrollo Punto 5")
time.sleep(1)

numeropunto5 = input ("Ingrese un número decimal: ")
numerosindecimal = int(float(numeropunto5))
print(numerosindecimal)

time.sleep(4)

'''
6. ¿Cuál es la salida de las siguientes expresiones?
1 != 2
Salida: True
True == 1
Salida: True
False != False
Salida: False
False > 0
Salida: False
1.0 < 1
Salida: False
“test” == “test”
Salida: True
1.0 >= 1
Salida: True
'''


'''
7. (Opcional) Escriba un programa que le pida al usuario que ingrese nombre y edad. Luego muestre un mensaje
donde le informe el año en que va a cumplir 100.
'''
print("Desarrollo Punto 7")
time.sleep(1)

print("ADVERTENCIA! SI USTED AUN NO CUMPLIO EN EL AÑO CORRIENTE EL PROGRAMA PUEDE FALLAR, PEDIMOS DISCULPAS")

time.sleep(5)

instruccionnombre = input("Ingrese su nombre: ")
edad7 = int(input("Ingrese su edad: "))
añoactual = int(input("Ingrese el año actual: "))

añosquefaltan = 100 - edad7
resultado = añoactual+añosquefaltan

print("El/La usuario " + instruccionnombre + " cumplirá 100 en el año " + str(resultado))

time.sleep(4)

'''
8. (Opcional) Escriba un programa que permita convertir una temperatura en Celsius a la escala Farenheit. La
fórmula es:
Fahrenheit = (9.0/5.0) x Celsius + 32
'''
print("Desarrollo Punto 8")
time.sleep(1)

temp_cel = int(input("Ingrese la temperatura en °C a convertir a °F: "))
temp_far = (9.0/5.0)* temp_cel + 32
print("El resultado es: " + str(temp_far) + "°F")

time.sleep(4)

'''
9. (Opcional) Calculadora simple: Cree un programa capaz de pedir dos números al usuario y devolver el resultado
de la suma, resta, multiplicación y división entre los mismos. Por ejemplo, si los números son 3 y 5, la calculadora
nos devolvería: 3+5; 3-5; 3*5 y 3/5. Pruebe también expandir su calculadora y agregar nuevas operaciones, tales
como la potenciación o la división entera.
'''
print("Desarrollo Punto 9")
time.sleep(1)

print("Iniciando calculadora...")
time.sleep(3)

num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))

suma = num1+num2
resta = num1-num2
multiplicacion = num1*num2
division = num1/num2
potencia = num1**num2
divent = num1//num2

print("Suma = " + str(suma))
print("Resta = " + str(resta))
print("Multiplicación = " + str(multiplicacion))
print("División = " + str(division))
print("Potencia = " + str(potencia))
print("División entera como el yogurt = " + str(divent))

time.sleep(10)