import time
# def funcion(para1, para2):
#     return para1, para2

# # valor1,valor2 = funcion("perro","gato")
# # print(valor1)
# # print(valor2)

# def hacer_remera(mensaje='me gusta python', talle ='XL'):
#     print('Su remera es talle', talle, 'y su mensaje es', mensaje)

# hacer_remera()


'''----------------------------------------------------------------------------------------------------------'''

listadeejemplo = ['a','b','c','d','e']
listadenumeros =[1,2,3,4,5,6,1,5,1]

print(listadeejemplo[4]) #Busca un elemento en la lista con [posición]
print(len(listadeejemplo)) #Con len(longitud) podemos saber la longitud de la misma

for i in range(len(listadeejemplo)):  #Podemos mostrar en la terminal cada uno de los elementos de la lista
    print(listadeejemplo[i])
    time.sleep(1)
    
listadepalabras = ['arbol', 'hoja', 'pasto', 'cielo']