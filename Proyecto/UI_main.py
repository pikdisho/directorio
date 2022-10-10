import tkinter
from turtle import bgcolor
from PIL import ImageTk, Image
import functions
from clases import *

timer_refresco=1000

user_preferences = import_user_data()
ancho, alto = user_preferences.get_ancho_alto()

main_window = tkinter.Tk()
establecer_preferencias = user_preferences.set_main_window_preferences(main_window)

# frame_logo = tkinter.Frame(main_window)
# tamano_frame_logo = ConfigurarFrame(frame_logo, 15, 10)
# frame_logo.config(bg='red')
# frame_logo.pack_propagate(False)
# frame_logo.pack()


frame_barra = tkinter.Frame(main_window)
tamano_barra = ConfigurarFrame(frame_barra, 15,100)
frame_barra.config(bg='green')
frame_barra.pack_propagate(False)
frame_barra.pack(side=tkinter.LEFT)

imagen_logo = Image.open(r'media\frame_logo.png')
imagen_logo = imagen_logo.resize((int(ancho*0.15), int(alto*0.1)), Image.Resampling.LANCZOS)
imagennn = ImageTk.PhotoImage(imagen_logo)
imagen_label = tkinter.Label(frame_barra, image=imagennn)
imagen_label.config(bg='#6d407f')
imagen_label.pack()


frame_reloj = tkinter.Frame(main_window)
tamano_reloj = ConfigurarFrame(frame_reloj,85,10)

frame_reloj.config(bg='blue')
frame_reloj.pack_propagate(False)
frame_reloj.pack()

saludo = str('!Buenos dias, ' + user_preferences.get_nombre())
saludo_variable = tkinter.StringVar(frame_reloj,value=saludo)

saludo_label = tkinter.Label(main_window, textvariable=saludo_variable, font='Consolas 40')
saludo_label.pack()
main_window.mainloop()


