'''
Para decisione smúltiples se usa elif
ej:
z=7

if z>8:
    print("algo")

    elif z>5:
            print("otra cosa")
    
    elif z<8:
            print("otra cosa")

    else
        print("otra cosa")

'''



suma=0
print("Ingrese cantidad nros a sumar: ")
n= int(input())

for i in range(n):
    print(f"Ingrese el numero {i+1}")
    numing= int(input())
    suma=suma+numing

print (suma)

