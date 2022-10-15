
with open (r'ejemplos_utiles\fichero.txt', 'r') as archivo_eventos:
    eventos_leidos_crudo = [linea.strip() for linea in archivo_eventos]
    eventos_leidos = [eventos.split("xd")[0] for eventos in eventos_leidos_crudo]

eventos_separados = []
for item in eventos_leidos:
    
    string = item.split("||")
    eventos_separados.append(string)
    
print(eventos_separados)
print(eventos_separados[0][1])

# Python3 code to demonstrate working of
# Validate String date format
# Using strptime()
from datetime import datetime
 
# initializing string
test_str = eventos_separados[0][1]
 
# printing original string
print("The original string is : " + str(test_str))
 
# initializing format
format = "%d/%m/%Y"
 
# checking if format matches the date
res = True
 
# using try-except to check for truth value
try:
    res = bool(datetime.strptime(test_str, format))
except ValueError:
    res = False
 
# printing result
print("Does date match format? : " + str(res))