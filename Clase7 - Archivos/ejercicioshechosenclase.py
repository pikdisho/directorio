# 1- Escribir un programa que abra un archivo, lea todas sus lineas y cuente cuantas lineas existen en el mismo.
# contador_lineas = 0
# with open('ola.txt', 'r+') as archivo_a_leer:
#     contenido_lineas = archivo_a_leer.readlines()
#     for item in contenido_lineas:
#         contador_lineas +=1
# print('El archivo tiene', (contador_lineas), 'lineas')

# Escriba una funcion sumaLineas(nombre_Archivo) que lea un archivo de texto que contiene exatamente un numero en cada linea y 
# devuelva la suma de estos numeros

def sumaLineas(nombre_Archivo):
    with open(nombre_Archivo, 'r') as archivo_de_numeros:
        suma=0
        lista_numeros = archivo_de_numeros.readlines()
        for items in lista_numeros:
            suma += int(items)
        print(suma)

sumaLineas(r'Clase7 - Archivos\numerosparaejercicio.txt')

# 3. Pedir al usuario que ingrese un nombre y un telefono. Si alguno de estos valores no son 
# ingresados correctamente, el programa debe ser capaz de manejarlo