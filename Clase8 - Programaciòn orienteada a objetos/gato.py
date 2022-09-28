from asyncio import gather
from telnetlib import GA


class Gato():
    def __init__(self, nombredelgato, edaddelgato, dueniodelgato):
        self.nombre=nombredelgato
        self.edad=edaddelgato
        self.duenio=dueniodelgato
        self.niveldecarinio=0
        
    def presentaciondelgato(self):
        print('Hola, soy un gato llamado', self.nombre, 'tengo', self.edad, 'años y mi dueño es', self.duenio)

    def carinio(self, gatocarinio):
        self.niveldecarinio = gatocarinio

    def acariciar(self):   
        self.niveldecarinio += 10
        print('*ronroneo ronroneo prpr*')
        print('Mi nivel de cariño es:', self.niveldecarinio)

    def mequieren(self):
        if (self.niveldecarinio >= 60):
            print('Mi dueño', self.duenio, 'me quiere mucho ♥')
        else:
            print('Mi dueño', self.duenio, 'no me quiere y me voy a escapar de su casa')

pepe = Gato('Pepe', '3', 'Franco')
pepe.carinio(10)

pepe.presentaciondelgato()
pepe.mequieren()
pepe.acariciar()
pepe.acariciar()
pepe.acariciar()
pepe.acariciar()
pepe.acariciar()
pepe.acariciar()

pepe.mequieren()

