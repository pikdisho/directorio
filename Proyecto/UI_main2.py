import tkinter
from PIL import ImageTk, Image
from functions import *
from clases import *

user_preferences = import_user_data()
ancho, alto = user_preferences.get_ancho_alto()

main_window = tkinter.Tk()
main_window.config(bg='#eff0f3')
establecer_preferencias = user_preferences.set_main_window_preferences(main_window)

hora_para_widget = hora_sola()


# ---------------------------------------------------------------------------------

frame_background = tkinter.Frame(main_window)
configurar_frame_background = ConfigurarFrame(frame_background, 100, 40)
frame_background.config(bg='#34304d')
frame_background.place(x=0, y=0)

imagen_bg = Image.open(r'media\fondo_dia.gif')
imagen_bg = imagen_bg.resize((int(ancho), int(alto*0.4)), Image.Resampling.LANCZOS)
imagen_para_poner = ImageTk.PhotoImage(imagen_bg)

label_bg = tkinter.Label(frame_background, image=imagen_para_poner)
label_bg.config(bg='#34304d')
label_bg.place(x=-1, y=0)

# ---------------------------------------------------------------------------------

frame_top = tkinter.Frame(main_window)
configurar_frame_top =  ConfigurarFrame(frame_top, 88,80)
frame_top.place(x=int(ancho*0.06), y=int(alto*0.22))
frame_top.config(bg='white')
frame_background.lower(frame_top)

variable_hora = tkinter.StringVar(frame_top, value=hora_completa())
label_reloj = tkinter.Label(frame_top, textvariable=variable_hora, font='Arial 45 bold')
label_reloj.config(bg='#7e7eb0')
label_reloj.place(x=40, y=30)

refresh_time = 1000
def refrescar_reloj():
    print("Refrescando!")
    variable_hora.set(hora_completa())
    frame_top.after(refresh_time, refrescar_reloj)


refrescar_reloj()
main_window.mainloop()


