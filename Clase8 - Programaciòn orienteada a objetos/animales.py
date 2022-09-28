class Animales():
    def __init__(self, especiedelanimal, nombredelanimal, edaddelanimal):
        self.especie = especiedelanimal
        self.nombre = nombredelanimal
        self.edad = edaddelanimal

    def presentacion(self):
        print('Hola soy un/una', self.especie, 'mi nombre es', self.nombre, 'y tengo', self.edad)


class Perro(Animales):
    def __init__(self, especiedelanimal, nombredelanimal, edaddelanimal, cantidaddepatas):
        super().__init__(especiedelanimal, nombredelanimal, edaddelanimal)
        self.patas = cantidaddepatas
