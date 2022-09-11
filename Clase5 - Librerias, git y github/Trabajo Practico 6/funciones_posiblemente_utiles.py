# Escriba una función redondear() que permita redondear un número
# decimal de acuerdo al criterio: Si el número es mayor a 3.50, devolver el
# entero siguiente (en este caso, 4), si no devolver el entero inmediatamente
# anterior (3). 

def redondear(numeroaredondear):
    decimal_numeroaredondear = numeroaredondear - int(numeroaredondear) 
    if (decimal_numeroaredondear < 0.5):
        return(int(numeroaredondear))
    else:
        return(int((numeroaredondear)+1))