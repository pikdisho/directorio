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

frame_barra = tkinter.Frame(main_window)
tamano_barra = ConfigurarFrame(frame_barra, 15,100)
frame_barra.config(bg='#7855AA')
frame_barra.pack_propagate(False)
frame_barra.pack(side=tkinter.LEFT)

imagen_logo = Image.open(r'media\logo.gif')
imagen_logo = imagen_logo.resize((int(ancho*0.15), int(alto*0.05)), Image.Resampling.LANCZOS)
imagennn = ImageTk.PhotoImage(imagen_logo)
imagen_label = tkinter.Label(frame_barra, image=imagennn)
imagen_label.config(bg='#6d407f')
imagen_label.pack()

frame_principal = tkinter.Frame(main_window)
tamano_frame_principal = ConfigurarFrame(frame_principal, 85,20)
frame_principal.config(bg='#f8e3ff')
frame_principal.pack_propagate(False)
frame_principal.pack()

label_bg = tkinter.Label(frame_principal, image=imagennn)

frame_reloj = tkinter.Frame(frame_principal)
tamano_reloj = ConfigurarFrame(frame_reloj,85,5)

frame_reloj.config(bg='#7855AA')
frame_reloj.pack_propagate(False)
frame_reloj.pack()


saludo = str('¡Buenos dias, ' + user_preferences.get_nombre() + '!')
saludo_variable = tkinter.StringVar(frame_reloj,value=saludo)

saludo_label = tkinter.Label(frame_principal, textvariable=saludo_variable, font='Arial 20 bold')
saludo_label.config(bg='green')
saludo_label.pack_propagate(False)
saludo_label.pack()


main_window.mainloop()


