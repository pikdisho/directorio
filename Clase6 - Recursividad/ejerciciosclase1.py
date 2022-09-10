def contadorsimple(numeroacontar):
    while numeroacontar >= 0:
        print(numeroacontar)
        numeroacontar -= 1

def contadorrecursividad(numeroacontar):
    if (numeroacontar == 0):
        print('0')
    else:
        print(numeroacontar)
        contadorrecursividad(numeroacontar-1)

def contadorrecursividadprofe(numeroacontar):
    print(numeroacontar)
    if (numeroacontar == 0):
        return (numeroacontar)
    else:
        return contadorrecursividadprofe(numeroacontar-1)


numeroelegido = int(input('→ Introduzca el numero: '))
contadorrecursividadprofe(numeroelegido)



