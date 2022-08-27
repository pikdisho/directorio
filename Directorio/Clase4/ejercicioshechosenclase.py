# Crea un programa que pida al usuario un número de mes (por ej el 4) y diga cuantos dias tiene (por ej 30) y el nombre del mes.
# Para simplificarlo vamos a suponer que febrero tiene 28 dias. Usar diccionarios


# meselegido = int(input('Ingrese un número de mes (1-12): '))-1
# diccionario_de_meses = {
#     'meses': ['Enero', 'Febrero', 'Marzo','Abril','Mayo','Junio','Julio','Agosto','Septiembre','Octubre','Noviembre','Diciembre'],
#     'duraciondelmes': [31,28,30,31,31,31,31,31,31,31,31,31]
#     }
    
# print('El nombre del mes elegido es', diccionario_de_meses['meses'][meselegido] ,'y tiene', diccionario_de_meses['duraciondelmes'][meselegido], 'dias')


# -------------------------------------------------------------------------------------------------------------------------

# Se quiere erealizar un programa que le apor tecclado las 7 notas obtenidas por un alumno (comprendidas entre 0 y 10)
# A continuacion debe mostrar todas las notas.

listadenotas=[]

for contadordenotas in range (7):
    listadenotas.append(int(input('Ingrese sus notas (1-10): ')))

print(listadenotas)

# Ahora contar cuantas notas aprobadas y cuantas notas desaprobadas tiene dicho alumno
contadoraprobadas=0
contadordesaprobadas=0

for notas in listadenotas:
    if notas >= 6:
        contadoraprobadas+=1
    elif notas < 6:
        contadordesaprobadas+=1

print('El usuario tiene', str(contadoraprobadas), 'notas aprobadas y', str(contadordesaprobadas), 'notas desaprobadas')

# Ahora obtener el promedio de estas notas. 

sumaparapromedio = 0

for notes in listadenotas:
    sumaparapromedio += notes

promedio = (sumaparapromedio/len(listadenotas))
print("promedio: ",promedio)

# OPCIONAL: Tambien indicar que tan cerca (o lejos esta ese promedio de un 8.0)

distancia = 8.0 - float(promedio)
print("distancia: ", abs(distancia))
