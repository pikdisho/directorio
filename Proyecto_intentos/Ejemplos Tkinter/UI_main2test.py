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

# imagen_bg = Image.open(r'media\fondo_tarde.gif')
# imagen_bg = imagen_bg.resize((int(ancho), int(alto*0.4)), Image.Resampling.LANCZOS)
# imagen_para_poner = ImageTk.PhotoImage(imagen_bg)

# label_bg = tkinter.Label(frame_background, image=imagen_para_poner)
# label_bg.config(bg='#34304d')
# label_bg.place(x=-1, y=0)

# ---------------------------------------------------------------------------------------

hora_para_tkinter = tkinter.StringVar(main_window, value=hora_sola())
hora_test = hora_sola()
string_tiempo_dia = tiempo_del_dia()

imagen_dia = Image.open(r'media\fondo_dia.gif')
imagen_dia = imagen_dia.resize((int(ancho), int(alto*0.4)), Image.Resampling.LANCZOS)
imagen_para_poner_dia = ImageTk.PhotoImage(imagen_dia)

imagen_tarde = Image.open(r'media\fondo_tarde.gif')
imagen_tarde = imagen_tarde.resize((int(ancho), int(alto*0.4)), Image.Resampling.LANCZOS)
imagen_para_poner_tarde = ImageTk.PhotoImage(imagen_tarde)

imagen_noche = Image.open(r'media\fondo_noche.gif')
imagen_noche = imagen_noche.resize((int(ancho), int(alto*0.4)), Image.Resampling.LANCZOS)
imagen_para_poner_noche = ImageTk.PhotoImage(imagen_noche)


label_bg = tkinter.Label(frame_background)
label_bg.place(x=-1, y=0)
canvastest = tkinter.Canvas(label_bg, width=int(ancho), height=int(alto*0.4))
canvastest.pack()
contenedortest = canvastest.create_image(0,0, image=imagen_para_poner_noche)

# def background_adaptable():
#     tiempo.refresh_hora()
#     if (string_tiempo_dia == 'maniana'):
#         print('mmm')
#         label_bg.config(bg='#34304d', image=imagen_para_poner_dia)
#         label_bg.place(x=-1, y=0)
#     if (string_tiempo_dia == 'tarde'):
#         print('ttt')
#         label_bg.config(bg='#34304d', image=imagen_para_poner_tarde)
#         label_bg.place(x=-1, y=0)
#     if (string_tiempo_dia == 'noche'):
#         print('nnn')
#         label_bg.config(bg='#34304d', image=imagen_para_poner_noche)
#         label_bg.place(x=-1, y=0)

testttt = tiempo.get_hora()

# def background_adaptable():
#     print('actualizando bg?')
#     if (testttt>0 and testttt<20):
#         print('mmm')
#         label_bg.config(bg='#34304d', image=imagen_para_poner_dia)
#         label_bg.place(x=-1, y=0)
#     if (testttt>21 and testttt<40):
#         print('ttt')
#         label_bg.config(bg='#34304d', image=imagen_para_poner_tarde)
#         label_bg.place(x=-1, y=0)
#     if (testttt>41 and testttt<60):
#         print('nnn')
#         label_bg.config(bg='#34304d', image=imagen_para_poner_noche)
#         label_bg.place(x=-1, y=0)


# ---------------------------------------------------------------------------------

frame_top = tkinter.Frame(main_window)
configurar_frame_top =  ConfigurarFrame(frame_top, 88,80)
frame_top.place(x=int(ancho*0.06), y=int(alto*0.22))
frame_top.config(bg='white')
frame_background.lower(frame_top)

# --------------------------------------------------------------------------------

variable_hora = tkinter.StringVar(frame_top, value=hora_completa())
label_reloj = tkinter.Label(frame_top, textvariable=variable_hora, font='Arial 45 bold')
configurar_label_reloj = ConfigurarColorAcentuacion(label_reloj, '#fdddd0')
label_reloj.place(x=40, y=30)

refresh_time = 1000
def refrescar_reloj():
    variable_hora.set(hora_completa())
    print('refrescando')
    frame_top.after(refresh_time, refrescar_reloj)
def refrescar_tiempo():
    tiempo.refresh_hora()
def refrescar_bg():
    tiempo.refresh_hora()
    print('olaaaaaaa')
    frame_background.after(refresh_time, refrescar_bg)
    frame_background.after(refresh_time, frame_background.update_idletasks)
#---------------------------------------------------------------------------------
print(hora_test)
refrescar_reloj()
refrescar_bg()
main_window.mainloop()


