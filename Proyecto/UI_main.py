import tkinter
from PIL import ImageTk, Image
import functions
timer_refresco=1000

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

frame_bienvenido = tkinter.Frame(main_window, width=ancho, height=int(alto*0.15))
frame_bienvenido.config(bg='#745fab')
frame_bienvenido.pack()

def refrescar_reloj():
    print('refrescando toy')
    hora.set(functions.hora())
    main_window.after(timer_refresco, refrescar_reloj)  
    
hora = tkinter.StringVar(frame_bienvenido, value=functions.hora())

hora_label = tkinter.Label(frame_bienvenido, textvariable=hora, font=f"Consolas 60")
refrescar_reloj()
hora_label.pack(side=tkinter.LEFT)


main_window.mainloop()


