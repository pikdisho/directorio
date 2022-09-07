#menu.py
#funcion para conocer si un numero es o no primo
def primo(x):
    primaso=True
    for i in range(2,x):
        if x%i == 0:
            primaso=False
            break
    if primaso:
        return " Es Primo"
    else:
        return " No es Primo"

#funcion para saber si un numero es par o no
def paridad(p):
    if p%2 == 0:
        return "Es Par"
    else:
        return "No es Par"

#funcion para saber si el numero es perfecto o no
def perfecto(y):
    ac=0
    for i in range(1,y):
        if y%i==0:
            ac+=i  #ac=ac+i
    if ac==y:
        return "Es Perfecto"
    else:
        return "No es Perfecto"

def factorial(z):
    i=1
    fac=1
    while i<=z:
        fac*=i # es lo mismo que fac=fac*i
        i+=1 # es lo mismo que i=i+1
    if z==0:
        fac=1
    return "Su Factorial es "+str(fac)


