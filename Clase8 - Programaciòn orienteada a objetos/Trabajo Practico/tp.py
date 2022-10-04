# 1) Escribir una clase llamada Rectángulo que contenga una base y una altura, y que contenga un método que devuelva el área
# del rectángulo.

class Rectangulo():
    def __init__(self, mi_base, mi_altura):
        self.base = mi_base
        self.altura = mi_altura

    def area_rectangulo(self):
        return(self.base*self.altura)

rectangulito = Rectangulo(3,2)

print(rectangulito.area_rectangulo())

# 2) Modelar una clase Mate que describa el funcionamiento de la conocida bebida tradicional argentina. La clase debe contener
# como miembros:
# o Un atributo para la cantidad de cebadas restantes hasta que se lava el mate (representada por un número).
# o Un atributo para el estado (lleno o vacío).
# o Un atributo n, que indica la cantidad máxima de cebadas.
# o Un método cebar, que llena el mate con agua. Si se intenta cebar con el mate lleno, se debe lanzar una
# excepción que imprima el mensaje ¡Cuidado! ¡Te quemaste!
# o Un método beber, que vacía el mate y le resta una cebada disponible. Si se intenta beber un mate vacío, se
# debe lanzar una excepción que imprima el mensaje: ¡El mate está vacío!
# o Es posible seguir cebando y bebiendo el mate aunque no haya cebadas disponibles. En ese caso la cantidad
# de cebadas restantes se mantendrá en 0, y cada vez que se intente beber se debe imprimir un mensaje de aviso:
# “Advertencia: el mate está lavado.” pero no se debe lanzar una excepción.

class Mate():
    def __init__(self, cebadas_actuales, estado_mate,):
        self.maximo_cebadas = 10
        self.cebadas_restantes = cebadas_actuales - self.maximo_cebadas
        self.estado 
        


