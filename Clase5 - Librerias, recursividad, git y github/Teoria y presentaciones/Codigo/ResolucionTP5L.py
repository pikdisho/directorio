"""
#Ejercicio 3
import datetime
import time
inicio=time.perf_counter()
def hora_fecha():
    hf=datetime.datetime.today()
    print(hf)

hora_fecha()

final=time.perf_counter()
print("tiempo de ejecución: ",final-inicio)
"""

"""#Ejercicio 4
import random
import time
inicio=time.perf_counter()
def azar():
    numero = random.randint(2,10)
    while numero % 2 != 0:
        numero = random.randint(2,10)
    return numero
print(azar())
final=time.perf_counter()
while True:
    print(azar())
    time.sleep(0.5)
"""
#print("tiempo de ejecución: ",final - inicio)

#Ejercicio 5
"""
import time
import random
lista= ["Es seguro que sí","Las chances son buenas","Puedes contar con ello","Pregúntame de nuevo más tarde","Concéntrate y pregunta de nuevo","No veo con claridad, intenta de nuevo","Mi respuesta es no","Mis fuentes me dicen que no"]
def magic_ball():
    return random.choice(lista)

print("MAGIC BALL\n")
p=input("Qué deseas saber? : ")
print(" ")
while p != "apagar":
    inicio=time.perf_counter()
    print(magic_ball())
    print(" ")
    print("Si ya no desea preguntar ingrese: apagar\n")
    p=input("¿Qué deseas saber?: ")
    print(" ")
    final=time.perf_counter()
    print("tiempo de ejecución: ",final-inicio)
    
print(" ")
print("Espero que te haya ayudado")
"""

#ejercicio 7
import random
print("Sorteo\n")
print("[PAPEL1,PAPEL2,PAPEL3,PAPEL4,PAPEL5,PAPEL6,PAPEL7,PAPEL8,PAPEL9,PAPEL10]")
papel=input("Detener la mezcla con la palabra ALTO: ")
while papel != 'salir':
    if papel == "ALTO":
        nombre=random.choice(['PAPEL1','PAPEL2','PAPEL3','PAPEL4','PAPEL5','PAPEL6','PAPEL7','PAPEL8','PAPEL9','PAPEL10'])
        print("el papel que agarraste es: ",nombre)
        d={'PAPEL1':'Juan','PAPEL2':'Mateo','PAPEL3':'Lucas','PAPEL4':'Pablo','PAPEL5':'Nehemías','PAPEL6':'Caleb','PAPEL7':'Josué','PAPEL8':'Noe','PAPEL9':'Marcos','PAPEL10':'Alberto'}
        print("y el ganador es ->",d[nombre])
        print("para terminar escriba salir")
        print()
        papel=input("Detener la mezcla con la palabra ALTO: ")

    else:
        print("La entrada ingresada es incorrecta")
        print("para terminar escriba salir")
        print()
        papel=input("Detener la mezcla con la palabra ALTO: ")
print("GRACIAS")

