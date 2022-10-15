import tkinter
from PIL import ImageTk, Image
from functions import *
from clases import *

user_preferences = import_user_data()
ancho, alto = user_preferences.get_ancho_alto()

main_window = tkinter.Tk()
main_window.config(bg='#eff0f3')
establecer_preferencias = user_preferences.set_main_window_preferences(main_window)

# ---------------------------------------------------------------------------------

frame_background = tkinter.Frame(main_window)
configurar_frame_background = ConfigurarFrame(frame_background, 100, 40)
frame_background.config(bg='#34304d')
frame_background.place(x=0, y=0)

# ---------------------------------------------------------------------------------------

imagen_dia = Image.open(r'media\fondo_dia.gif')
imagen_dia = imagen_dia.resize((int(ancho), int(alto*0.4)), Image.Resampling.LANCZOS)
imagen_para_poner_dia = ImageTk.PhotoImage(imagen_dia)

imagen_tarde = Image.open(r'media\fondo_tarde.gif')
imagen_tarde = imagen_tarde.resize((int(ancho), int(alto*0.4)), Image.Resampling.LANCZOS)
imagen_para_poner_tarde = ImageTk.PhotoImage(imagen_tarde)

imagen_noche = Image.open(r'media\fondo_noche.gif')
imagen_noche = imagen_noche.resize((int(ancho), int(alto*0.4)), Image.Resampling.LANCZOS)
imagen_para_poner_noche = ImageTk.PhotoImage(imagen_noche)

horatk = tkinter.StringVar(main_window, value=hora_sola())

label_bg = tkinter.Label(frame_background)
label_bg.place(x=-1, y=0)


def background_adaptable():
    global color_adaptable
    if (int(horatk.get())>=6 and int(horatk.get())<13):
        print('Es de mañana')
        label_bg.config(bg='#34304d', image=imagen_para_poner_dia)
        color_adaptable = '#a29ec4'
    elif (int(horatk.get())>=13 and int(horatk.get())<20):
        print('Es de tarde')
        label_bg.config(bg='#34304d', image=imagen_para_poner_tarde)
        color_adaptable = '#d0673a'
    elif (int(horatk.get())>=20 and int(horatk.get())<60) or (int(horatk.get())>=0 and int(horatk.get())<6):
        print('Es de noche')
        color_adaptable = '#675e7b'
        label_bg.config(bg='#34304d', image=imagen_para_poner_noche)

background_adaptable()
# ---------------------------------------------------------------------------------

frame_top = tkinter.Frame(main_window)
configurar_frame_top =  ConfigurarFrame(frame_top, 88,80)
frame_top.place(x=int(ancho*0.06), y=int(alto*0.22))
frame_top.config(bg='white')
frame_background.lower(frame_top)

# --------------------------------------------------------------------------------

variable_hora = tkinter.StringVar(frame_top, value=hora_completa())
label_reloj = tkinter.Label(frame_top, textvariable=variable_hora, font='Arial 45 bold', fg='white')
configurar_label_reloj = ConfigurarColorAcentuacion(label_reloj, color_adaptable)
label_reloj.place(x=40, y=30)

# ----------------------------------------------------------------------------------

frame_reloj = tkinter.Frame(frame_top)
configurar_frame_reloj = ConfigurarFrame(frame_reloj, 25,20)
# frame_reloj.place(x=100,y=20)

# ----------------------------------------------------------------------------------

localidad_clima, tiempo_clima, info_clima, clima_clima = weather(ciudad_guardada)
print(localidad_clima)



#----------------------------------------------------------------------
def refrescar_reloj():
    variable_hora.set(hora_completa())
    frame_top.after(1000, refrescar_reloj)

def refrescar_bg():
    horatk.set(hora_sola())
    frame_background.after(1000, refrescar_bg)
    frame_background.after(1000, background_adaptable)
#---------------------------------------------------------------------------------

refrescar_reloj()
refrescar_bg()

main_window.mainloop()