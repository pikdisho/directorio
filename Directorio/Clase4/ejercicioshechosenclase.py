# Crea un programa que pida al usuario un número de mes (por ej el 4) y diga cuantos dias tiene (por ej 30) y el nombre del mes.
# Para simplificarlo vamos a suponer que febrero tiene 28 dias. Usar diccionarios

from logging.config import dictConfig


meselegido = int(input('Ingrese un número de mes: '))
diccionario_de_meses = {
    'meses': ['Enero', 'Febrero', 'Marzo'],
    'duraciondelmes': [31,28,30]

    }
    

}

print('El mes elegido tiene', diccionario_de_meses)