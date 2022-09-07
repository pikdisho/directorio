##Recursividad
"""
Una funcion es recursiva cuando se llama a si misma en algun momento de su definicion.
Usualmente existen soluciones no recursivas (llamadas iterativas porque incluyen alguna estructura repetitiva) para cada funcion recursiva, pero estas pueden ser mas faciles de leer y escribir, aunque tambien pueden ser mucho mas lentas en algunos casos
Toda funcion recursiva debe incluir un caso base, que es aquel donde la funcion no se vuelve a llamar a si misma, similar a como tenemos que asegurarnos que un ciclo while termine en algun momento
"""

##Ejemplo: Factorial
#n! = n * (n-1)!, if n > 1 and 0! = 1
'''
#recursivo
def factorial(n):
    if n == 0: #Caso base
        return 1
    else:
        return n * factorial(n-1)

#iterativo
def iterative_factorial(n):
    result = 1
    for i in range(2,n+1):
        result *= i
    return result
'''
#factorial(40)
#iterative_factorial(40)

##Ejemplo: Potencia de un numero

#iterativo
def potencia_i(base, exp):
    ans=1
    if exp==0:
        return ans
    else:
        while exp>=1:
            ans*=base
            exp-=1
        return ans

#recursivo
def potencia_r(base, exp):
    if exp==0:  #Caso base
        return 1
    elif exp==1:
        return base
    else:
        return base*potencia_r(base,exp-1)

#print("recursivo", potencia_r (5,3))
#print()
#print("iterativo", potencia_i (5, 3))

##Ejemplo: Fibonacci
#Serie de Fibonacci: Secuencia de numeros donde cada elemento n es igual a la suma de los dos elementos anteriores n-1 y n-2
#Este es un ejemplo en el que la recursividad no es recomendable: Para numeros >= 40, la version recursiva tarda millones de veces mas que la iterativa!!
"""
def fibr(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibr(n-1) + fibr(n-2)

def fibi(n):
    old, new = 0, 1
    if n == 0:
        return 0
    for i in range(n-1):
        old, new = new, old + new
    return new

print(fibi(50))
print(fibr(50))
"""
