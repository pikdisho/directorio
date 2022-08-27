from ast import match_case
import time

def ejerciciostp3(ejercicioelegido):
    # ejercicioelegido = int(input('Bienvenido a la corrección, escriba el nro de ejercicio que desea ejecutar'))
    match ejercicioelegido:
        case 1:
            ejercicio1()
        case 2:
            ejercicio2()
        case 3:
            ejercicio3()


# 1) Meter los números del 1 al 20 en una lista y mostrarla en pantalla. Hacer lo mismo para
# un rango de números indicado por un usuario.

def ejercicio1():
    print('Ejercicio 1')
    time.sleep(1)

    lista_para_hacer_el_ejercicio = []

    for i in range (1,36,):
        lista_para_hacer_el_ejercicio.append(i)

    print(lista_para_hacer_el_ejercicio)

    time.sleep(1)

    numeroinicial = int(input('Ingrese el primer numero a mostrar: '))
    numerofinal = int(input('Ingrese el numero final: '))
    lista_para_hacer_el_ejercicio_parte2 = []

    for j in range (numeroinicial, numerofinal+1):
        lista_para_hacer_el_ejercicio_parte2.append(j)

    print(lista_para_hacer_el_ejercicio_parte2)


# 2) Pide un número y guarda en una lista su tabla de multiplicar hasta el 10. Por ejemplo, si
# pide el 5 la lista tendrá: 5,10,15,20,25,30,35,40,45,50
def ejercicio2():
    print('Ejercicio 2')
    time.sleep(1)

    numeropunto2 = int(input('Introduzca el número a multiplicar: '))
    listamultiplicacionpunto2 = []
    memonumeropunto2 = numeropunto2
    while True:
        for i in range(1,11):
            memonumeropunto2 = numeropunto2 * i
            listamultiplicacionpunto2.append(memonumeropunto2)
            memonumeropunto2 = numeropunto2
        print(listamultiplicacionpunto2)
        break

# 3) Pide una cadena (string) por teclado, mete los caracteres en una lista sin repetir
# caracteres.

def ejercicio3():
    print('Ejercicio 3')
    time.sleep(1)

    listapunto3 = []
    cadenapunto3 = input('Ingrese una palabra o frase: ')
    
    for letras in range(len(cadenapunto3)):
        lista




























while True:
    ejercicioelegido = int(input('Por favor, escriba el número del ejercicio que desea ejecutar (1-12): '))
    ejerciciostp3(ejercicioelegido)
    repetir = input('¿Desea revisar otro ejercicio? (Y/N): ')
    if repetir == 'N' or repetir == 'n':
        print('Hasta la próxima, que le vaya bien')
        break
    


























# 2) Pide un número y guarda en una lista su tabla de multiplicar hasta el 10. Por ejemplo, si
# pide el 5 la lista tendrá: 5,10,15,20,25,30,35,40,45,50
# 3) Pide una cadena (string) por teclado, mete los caracteres en una lista sin repetir
# caracteres.
# 4) Pide una cadena (string) por teclado, mete los caracteres en una lista sin espacios.
# 5) Crea una tupla con números, pide un numero por teclado e indica cuantas veces se
# repite.
# 6) Crea una tupla con los meses del año, pedir números al usuario. Si el numero esta entre
# 1 y la longitud máxima de la tupla, muestra el contenido de esa posición sino muestra
# un mensaje de error. El programa termina cuando el usuario introduce un cero
# 7) Crea una tupla con números e indica el número con mayor valor y el que menor tenga.
# 8) Escribir una función que reciba una cadena y devuelva un diccionario con la cantidad de
# apariciones de cada palabra en la cadena. Por ejemplo, si recibe "Qué lindo día que hace
# hoy" debe devolver: 'que': 2, 'lindo': 1, 'día': 1, 'hace': 1, 'hoy': 1
# 9) Escribir un programa que vaya solicitando al usuario que ingrese nombres.
# - Si el nombre se encuentra en la agenda (implementada con un diccionario), debe
# mostrar el teléfono y, opcionalmente, permitir modificarlo si no es correcto.
# - Si el nombre no se encuentra, debe permitir ingresar el teléfono correspondiente. El
# usuario puede utilizar la cadena "*", para salir del programa