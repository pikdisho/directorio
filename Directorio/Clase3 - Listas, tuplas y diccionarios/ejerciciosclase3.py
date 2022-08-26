'''Solicitar al usuario que ingrese su dirección email, imprimir un mensaje indiando si la dirección es válida o no, valiendose de una función para decidirlo.
Una dirección se considerará valida si contiene @'''




# def verificaremail(email):
#     emailvalido = email.find ('@')
#     if emailvalido<0:
#         print("La dirección introducida no es válida")   
#     else:
#         print("Su dirección es válida")

# email = input('Ingrese su dirección email: ')
# verificaremail(email)


'''Meter los números del 1 al 35 en una lista y mostrarla en pantalla. Hacer lo mismo para un rango de números indicado por un usuario'''


lista_para_hacer_el_ejercicio = []

for i in range (1,36,):
    lista_para_hacer_el_ejercicio.append(i)

print(lista_para_hacer_el_ejercicio)


numeroinicial = int(input('Ingrese el primer numero a mostrar: '))
numerofinal = int(input('Ingrese el numero final: '))
lista_para_hacer_el_ejercicio_parte2 = []

for j in range (numeroinicial, numerofinal+1):
    lista_para_hacer_el_ejercicio_parte2.append(j)

print(lista_para_hacer_el_ejercicio_parte2)