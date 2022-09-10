from menú import paridad, perfecto, factorial, primo
print("BIENVENIDO A LA MÁQUINA DE CÁLCULO\n")
print("HAY DISTINTAS FUNCIONES, INGRESE SU NÚMERO Y LUEGO DECIDA QUÉ DESEA CONOCER\n")
numero=int(input("Ingrese un número: "))
print("a : Conocer si es o no un número par")
print("b : Conocer si es o no un número primo")
print("c : Conocer si es o no un número perfecto")
print("d : Conocer su factorial")
print("x : Salir\n")
opcion=input("escoja una opción: ")
while opcion != "x":
    if not "a"<=opcion<="d":
        print("La opción escogida es incorrecta, intentalo de nuevo")
        opcion=input("escoja una opción: ")
    while "a"<=opcion<="d":
        if opcion == "a":
            print(paridad(numero))
        elif opcion == "b":
            print(primo(numero))
        elif opcion == "c":
            print(perfecto(numero))
        elif opcion == "d":
            print(factorial(numero))
        opcion=input("escoja una opción: ")
print("Gracias, hasta luego")


    
