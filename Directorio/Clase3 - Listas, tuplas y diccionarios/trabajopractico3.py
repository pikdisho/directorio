from ast import Str, match_case
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
        case 4:
            ejercicio4()
        case 5:
            ejercicio5()
        case 6:
            ejercicio6()
        case 7:
            ejercicio7()
        case 8:
            ejercicio8()
        case 9:
            ejercicio9()



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
    
    for letras in cadenapunto3:
        if letras not in listapunto3:
            listapunto3+=letras

    print(listapunto3)


# 4) Pide una cadena (string) por teclado, mete los caracteres en una lista sin espacios.

def ejercicio4():
    print('Ejercicio 4')
    time.sleep(1)

    print('Work in progress')


# 5) Crea una tupla con números, pide un numero por teclado e indica cuantas veces se
# repite.

def ejercicio5():
    print('Ejercicio 5')
    time.sleep(1)

    contador = 0
    tuplapunto5 = (1,1,1,2,3,4,5,6,7,7,7,8,8,9,9,10,11,11,11,11,12,12,13,14,15,16,17,17,18,19,20,20,20,20,20)
    numeroabuscar = int(input ('Ingrese un numero para consultar cuantas veces se repite en la tupla (1-20): '))

    for numerorevisado in tuplapunto5:
        if (numerorevisado == numeroabuscar):
            contador +=1
    if (contador > 0):
        print('El número', str(numeroabuscar), 'se repite en la tupla', str(contador), 'veces' )
    elif (contador ==1):
        print('El número', str(numeroabuscar), 'se repite en la tupla una vez' ) 
    else:
            print('El número ingresado no se encuentra en la tupla')


# 6) Crea una tupla con los meses del año, pedir números al usuario. Si el numero esta entre
# 1 y la longitud máxima de la tupla, muestra el contenido de esa posición sino muestra
# un mensaje de error. El programa termina cuando el usuario introduce un cero

def ejercicio6():
    print('Ejercicio 6')
    time.sleep(1)

    tuplameses = ('Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre')
    switchpunto6=1
    respuestapunto6=0

    while (switchpunto6 ==1):
        numerousuariopunto6 = int(input('Ingrese un número para mostrar que elemento se encuentra en esa posición o ingrese 0 para finalizar: '))
        if (numerousuariopunto6>0 and numerousuariopunto6<len(tuplameses)+1):
            print('En la posición', str(numerousuariopunto6), 'se encuentra el elemento', tuplameses[numerousuariopunto6-1])
            numerousuariopunto6 = 0
        elif (numerousuariopunto6==0):
            print('El programa finalizo.')
            switchpunto6 = 0
        else:
            print('ERROR: El número ingresado no tiene una posición que le corresponda en la tupla')
        
# 7) Crea una tupla con números e indica el número con mayor valor y el que menor tenga.
def ejercicio7():
    print('Ejercicio 7')
    time.sleep(1)

    tuplaconmuchosnumeros = (1,5,7,8,9,6,20,15,50,70,90,60,30,50,55,66,91,100,200,0)
    posiblemayor = 0
    posiblemenor = 0

    print(tuplaconmuchosnumeros)
    for numeros in tuplaconmuchosnumeros:
        if (numeros>posiblemayor):
            posiblemayor = numeros
        elif (numeros<posiblemenor):
            posiblemenor = numeros
    print ('El numero mayor es', str(posiblemayor), 'y el numero menor es', str(posiblemenor))

# 8) Escribir una función que reciba una cadena y devuelva un diccionario con la cantidad de
# apariciones de cada palabra en la cadena. Por ejemplo, si recibe "Qué lindo día que hace
# hoy" debe devolver: 'que': 2, 'lindo': 1, 'día': 1, 'hace': 1, 'hoy': 1

def ejercicio8():
    print('Ejercicio 8')
    time.sleep(1)

    print('Work in progress, leyendo diccionarios...')

# 9) Escribir un programa que vaya solicitando al usuario que ingrese nombres.
# - Si el nombre se encuentra en la agenda (implementada con un diccionario), debe
# mostrar el teléfono y, opcionalmente, permitir modificarlo si no es correcto.
# - Si el nombre no se encuentra, debe permitir ingresar el teléfono correspondiente. El
# usuario puede utilizar la cadena "*", para salir del programa

def ejercicio9():
    print('Ejercicio 9')
    time.sleep(1)

    print('Work in progress, pedimos disculpas')




















while True:
    ejercicioelegido = int(input('Por favor, escriba el número del ejercicio que desea ejecutar (1-9): '))
    ejerciciostp3(ejercicioelegido)
    repetir = input('¿Desea revisar otro ejercicio? (Y/N): ')
    if repetir == 'N' or repetir == 'n':
        print('Hasta la próxima, que le vaya bien')
        break
    





























