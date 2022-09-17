# Escriba una función redondear() que permita redondear un número
# decimal de acuerdo al criterio: Si el número es mayor a 3.50, devolver el
# entero siguiente (en este caso, 4), si no devolver el entero inmediatamente
# anterior (3). 

def redondear(numeroaredondear):  
    if (numeroaredondear - int(numeroaredondear) < 0.5):
        return(int(numeroaredondear))
    else:
        return(int((numeroaredondear)+1))

print(redondear(3.5))