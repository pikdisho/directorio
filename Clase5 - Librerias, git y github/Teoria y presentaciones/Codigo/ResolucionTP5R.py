#ejercicio 1


#(a)
"""def rfunc1(n):
    return n + rfunc1(n-1)
"""
# En esta función no hay declarado un caso base,
# por lo que se prducirán infinitas llamadas.
#(b) 

"""def rfunc2(n):
    # solo para n<0
    if n == 0:
        return 1
    return n + rfunc2(n+1)
print(rfunc2(3))
"""
# aqui no se establece una precondicion, entonces
"""
 al momento de pasarle un numero positivo, la funcion
 nunca llega al caso base, y hace excede la cantidad máxima
 de llamadas.
"""

#Ejercicio 2
#recursiva
# si n es entero --> n+(n-1)
"""def suma_entero(n):
    if n==0: #caso base / 
        return 0
    if n>0:
        return n + suma_entero(n-1) #4+suma_entero(3)   4+3suma_entero(2)    4+3+2+suma_entero(1)
                                        # 4+3+2+1+suma_entero(0)    4+3+2+1+0
    else:
        return n + suma_entero(n+1)
print(suma_entero(8))
"""
#iterativa
"""def s_ent(n):
    sumador=0
    if n > 0:
        for i in range(0,n+1):
            sumador+=i
    else:
        for i in range(n,0+1):
            sumador+=i
    return sumador
print(s_ent(6))

"""

#Ejercicio 3
#iterativa

def es_pari(x):
    c=0
    for i in range(x,0,-2):
        c+=1
    return c == x/2
print(es_pari(31))


# n es par si el resto es cero // n es par si la cantidad de restas por 2 es igual a n/2 
def es_parr(n):
    if n == 2:
        return True
    elif n == 1:
        return False
    else:
        n=n-2
        return es_parr(n)

print(es_parr(31))

