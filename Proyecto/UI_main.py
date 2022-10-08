import tkinter
from PIL import ImageTk, Image

class preferences():    
    def __init__(self):
        with open(r'Proyecto\preferences\nombre_usuario.txt', 'r') as archivo_nombre:
            self.nombre = archivo_nombre.readline()
        with open(r'Proyecto\preferences\resolucion_usuario.txt', 'r') as archivo_resolucion:
            self.resolucion = archivo_resolucion.readline()
    def get_nombre(self):
        return(self.nombre)
    def get_resolucion(self):
        return(self.resolucion)
    def get_ancho_alto(self):
        ancho = int(self.resolucion[0:4]) # PARA PODER REDIMENSIONAR EL TAMAñO DE LOS FRAMES E IMAGENES
        alto = int(self.resolucion[5:9])
        return(ancho, alto)

user_preferences = preferences()
ancho, alto = user_preferences.get_ancho_alto()

class establecer_preferencias_ventana():
    def __init__(self, ventana_a_crear):
        ventana_a_crear.geometry(user_preferences.get_resolucion())
        ventana_a_crear.title('pikWidget')
        ventana_a_crear.resizable(0,0)
        ventana_a_crear.iconbitmap('wm', r'Proyecto\media\favicon.ico')

main_window = tkinter.Tk()
establecer_preferencias = establecer_preferencias_ventana(main_window)
main_window.mainloop()


