import tkinter
from tkinter import messagebox
from PIL import ImageTk, Image
from functions import *
from clases import *
# from datetime import date, datetime
import datetime

obtener_fecha = datetime.datetime.today()

fecha = obtener_fecha.strftime('%d/%m/%Y')

user_preferences = import_user_data()
ancho, alto = user_preferences.get_ancho_alto()

main_window = tkinter.Tk()
main_window.config(bg='#eff0f3')
establecer_preferencias = user_preferences.set_main_window_preferences(main_window)
# main_window.attributes('-fullscreen', True)
# ---------------------------------------------------------------------------------

fuente_reloj = ''
fuente_clima_grados = ''
fuente_clima_info = ''
fuente_clima_tiempo = ''
fuente_clima_localidad = ''

if ancho == 1920:
    print('La resolucion elegida es: 1920x1080')
    fuente_reloj = 'Arial 70 bold'
    fuente_clima_grados = 'Arial 70 bold'
    fuente_clima_info = 'Arial 18 '
    fuente_clima_tiempo = 'Arial 16 '
    fuente_clima_localidad = 'Arial 18 bold'
    fuente_tarea = 'Arial 21 bold'
    fuente_bienvenida = 'Arial 20 bold'
    fuente_flechas = 'Arial 28 bold'

elif ancho == 1366:
    print('La resolucion elegida es: 1366X768')
    fuente_reloj = 'Arial 49 bold'
    fuente_clima_grados = 'Arial 52 bold'
    fuente_clima_info = 'Arial 12'
    fuente_clima_tiempo = 'Arial 10 '
    fuente_clima_localidad = 'Arial 15 bold'
    fuente_tarea = 'Arial 15 bold'
    fuente_bienvenida = 'Arial 17 bold'
    fuente_flechas = 'Arial 23 bold'
elif ancho == 1280:
    print('La resolucion elegida es: 1280X720')
    fuente_reloj = 'Arial 47 bold'
    fuente_clima_grados = 'Arial 50 bold'
    fuente_clima_info = 'Arial 12'
    fuente_clima_tiempo = 'Arial 11'
    fuente_clima_localidad = 'Arial 14 bold'
    fuente_tarea = 'Arial 13 bold'
    fuente_bienvenida = 'Arial 15 bold'
    fuente_flechas = 'Arial 20 bold'

# --------------------------------------------------------------------------------

frame_background = tkinter.Frame(main_window)
label_bg = tkinter.Label(frame_background)

frame_top = tkinter.Frame(main_window)
frame_reloj = tkinter.Frame(frame_top)
variable_hora = tkinter.StringVar(frame_top, value=hora_completa())
label_fondo_reloj = tkinter.Label(frame_reloj)
label_reloj = tkinter.Label(frame_reloj, textvariable=variable_hora, font=fuente_reloj, fg='white')
label_reloj.lift(label_fondo_reloj)

horatk = tkinter.StringVar(main_window, value=hora_sola())
label_bg = tkinter.Label(frame_background)

frame_clima = tkinter.Frame(frame_top, bg='white')
label_fondo_clima = tkinter.Label(frame_clima)

variable_ciudad_guardada = tkinter.StringVar(main_window, value=ciudad_guardada)

localidad_clima, tiempo_clima, info_clima, clima_grados = 'null', 'null', 'null', 'null'

variable_grados = tkinter.StringVar(frame_clima, value=clima_grados)
variable_info = tkinter.StringVar(frame_clima, value=info_clima)
variable_tiempo = tkinter.StringVar(frame_clima, value=tiempo_clima)
variable_localidad = tkinter.StringVar(frame_clima, value=localidad_clima)

clima_grados_label = tkinter.Label(frame_clima, textvariable=variable_grados, font=fuente_clima_grados, fg='white')
clima_info_label = tkinter.Label(frame_clima, textvariable=variable_info, font=fuente_clima_info, fg='white')
clima_tiempo_label = tkinter.Label(frame_clima, textvariable=variable_tiempo, font=fuente_clima_tiempo, fg='white')
clima_localidad_label = tkinter.Label(frame_clima, textvariable=variable_localidad, font=fuente_clima_localidad, fg='white')

boton_configurar_clima = tkinter.Button(frame_clima, text='«', font=fuente_clima_localidad, fg='white', relief='flat', overrelief='raised', command=lambda:label_nuevo())
frame_introducir_nombreciudad = tkinter.Frame(frame_top)
frame_introducir_nombreciudad.config(bg='#545464')
configurar_frame_introducir_ciudad = ConfigurarFrame(frame_introducir_nombreciudad, 30, 15)
frame_top.lower(frame_introducir_nombreciudad)

label_introducir_ciudad = tkinter.Label(frame_introducir_nombreciudad, text='Introduce tu ciudad para configurar el clima:', font=fuente_clima_info, fg='white', bg='#545464')
entry_ciudad = tkinter.Entry(frame_introducir_nombreciudad, justify=tkinter.CENTER, font=fuente_clima_info, relief='solid')
boton_aceptar_ciudad = tkinter.Button(frame_introducir_nombreciudad, text='CONFIRMAR Y GUARDAR', font=fuente_clima_tiempo, fg='white', overrelief='flat', relief='raised', bg='#545464', command=lambda:destruir_label_nuevo())

lista_meses = [0, 'Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre']

mes_actual = int(obtener_fecha.strftime('%m'))
anio_actual = int(obtener_fecha.strftime('%Y'))
mes_string = lista_meses[mes_actual] + ' '+ str(anio_actual) 

frame_mes = tkinter.Frame(frame_top, bg='#e8e8e8')
mes_variable = tkinter.StringVar(frame_mes, value=mes_string)
label_mes_pantalla = tkinter.Label(frame_mes, textvariable=mes_variable, font=fuente_bienvenida, fg='white')
boton_mes_izquierda = tkinter.Button(frame_mes, text='←', font=fuente_flechas, fg='white', overrelief='flat', relief='raised', command=lambda: cambiar_mes('Izquierda'))
boton_mes_derecha = tkinter.Button(frame_mes, text='→', font=fuente_flechas, fg='white', overrelief='flat', relief='raised', command=lambda: cambiar_mes('Derecha'))


def label_nuevo():
    frame_introducir_nombreciudad.place(x=int(ancho/3.5), y=int(alto/40))
    label_introducir_ciudad.place(x=int(ancho*0.025), y=int(alto*0.02))
    entry_ciudad.place(x=int(ancho*0.075), y=int(alto*0.065))
    boton_aceptar_ciudad.place(x=int(ancho*0.074), y=int(alto*0.1))

def destruir_label_nuevo():
    frame_introducir_nombreciudad.place(x=-1000, y=-1000)
    definir_ubicacion(entry_ciudad.get())
    refrescar_clima()

# ---------------------------------------------------------------------------------

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

label_redondeado_dia = Image.open(r'media\label_dia.gif')
label_redondeado_dia = label_redondeado_dia.resize((int(ancho*0.25), int(alto*0.15)), Image.Resampling.LANCZOS)
colocar_label_dia = ImageTk.PhotoImage(label_redondeado_dia)

label_redondeado_tarde = Image.open(r'media\label_tarde.gif')
label_redondeado_tarde = label_redondeado_tarde.resize((int(ancho*0.25), int(alto*0.15)), Image.Resampling.LANCZOS)
colocar_label_tarde = ImageTk.PhotoImage(label_redondeado_tarde)

label_redondeado_noche = Image.open(r'media\label_noche.gif')
label_redondeado_noche = label_redondeado_noche.resize((int(ancho*0.25), int(alto*0.15)), Image.Resampling.LANCZOS)
colocar_label_noche = ImageTk.PhotoImage(label_redondeado_noche)

label_bg.place(x=-1, y=0)

# COLOR DIA = #6c6ca3
# COLOR TARDE = #d2663a
# COLOR NOCHE = #3c3c5c

def background_adaptable():
    global color_adaptable
    if (int(horatk.get())>=6 and int(horatk.get())<13):
        color_adaptable = '#6c6ca3'
        label_bg.config(bg='#6c6ca3', image=imagen_para_poner_dia)       
        label_reloj.config(bg=color_adaptable)
        label_fondo_reloj.config(bg='white', image=colocar_label_dia)
        label_fondo_clima.config(bg='white', image=colocar_label_dia)

        clima_grados_label.config(bg=color_adaptable)
        clima_info_label.config(bg=color_adaptable)
        clima_tiempo_label.config(bg=color_adaptable)
        clima_localidad_label.config(bg=color_adaptable)
        boton_configurar_clima.config(bg=color_adaptable)
        label_mes_pantalla.config(bg=color_adaptable)
        boton_mes_izquierda.config(bg=color_adaptable)
        boton_mes_derecha.config(bg=color_adaptable)

    elif (int(horatk.get())>=13 and int(horatk.get())<20):
        color_adaptable = '#d2663a'
        label_bg.config(bg='#d2663a', image=imagen_para_poner_tarde) 
        label_reloj.config(bg='#d2663a')
        label_fondo_reloj.config(bg='white', image=colocar_label_tarde)
        label_fondo_clima.config(bg='white', image=colocar_label_tarde)

        clima_grados_label.config(bg=color_adaptable)
        clima_info_label.config(bg=color_adaptable)
        clima_tiempo_label.config(bg=color_adaptable)
        clima_localidad_label.config(bg=color_adaptable)
        boton_configurar_clima.config(bg=color_adaptable)
        label_mes_pantalla.config(bg=color_adaptable)
        boton_mes_izquierda.config(bg=color_adaptable)
        boton_mes_derecha.config(bg=color_adaptable)

    elif (int(horatk.get())>=20 and int(horatk.get())<60) or (int(horatk.get())>=0 and int(horatk.get())<6):
        color_adaptable = '#3c3c5c'
        label_reloj.config(bg='#3c3c5c')
        label_bg.config(bg='#3c3c5c', image=imagen_para_poner_noche)
        label_fondo_reloj.config(bg='white', image=colocar_label_noche)
        label_fondo_clima.config(bg='white', image=colocar_label_noche)

        clima_grados_label.config(bg=color_adaptable)
        clima_info_label.config(bg=color_adaptable)
        clima_tiempo_label.config(bg=color_adaptable)
        clima_localidad_label.config(bg=color_adaptable)
        boton_configurar_clima.config(bg=color_adaptable)
        label_mes_pantalla.config(bg=color_adaptable)
        boton_mes_izquierda.config(bg=color_adaptable)
        boton_mes_derecha.config(bg=color_adaptable)

background_adaptable()
# ---------------------------------------------------------------------------------

configurar_frame_top =  ConfigurarFrame(frame_top, 88,80)
frame_top.place(x=int(ancho*0.06), y=int(alto*0.22))
frame_top.config(bg='white')
frame_background.lower(frame_top)

# --------------------------------------------------------------------------------

label_reloj.place(x=int(ancho*0.059), y=(alto*0.025))

# ----------------------------------------------------------------------------------

configurar_frame_reloj = ConfigurarFrame(frame_reloj, 25,15)
frame_reloj.place(x=int(ancho*0.027),y=int(alto*0.02))
label_fondo_reloj.pack()

# ----------------------------------------------------------------------------------

configurar_frame_clima = ConfigurarFrame(frame_clima, 25,15)
frame_clima.place(x=int(ancho*0.597),y=int(alto*0.02))
label_fondo_clima.pack()

clima_grados_label.lift(label_fondo_clima)

clima_grados_label.place(x=int(ancho*0.015), y=int(alto*0.011))
clima_localidad_label.place(x=int(ancho*0.1), y=int(alto*0.021))
clima_tiempo_label.place(x=int(ancho*0.1), y=int(alto*0.056))
clima_info_label.place(x=int(ancho*0.015), y=int(alto*0.112))

boton_configurar_clima.place(x=int(ancho*0.228), y=int(alto*0.06))

#----------------------------------------------------------------------

def generar_ventana_agregar_tarea():
    ancho_ventana_agregar = int(ancho/2.4)
    alto_ventana_agregar = int(alto/4)
    resolucion_ventana_agregar = (str(ancho_ventana_agregar) + 'x' + str(alto_ventana_agregar))
    posicionx = '+'+str(int(ancho/2))
    posiciony = '+'+str(int(alto/2))

    ventana_agregar = tkinter.Toplevel()
    ventana_agregar.geometry(resolucion_ventana_agregar+posicionx+posiciony)
    ventana_agregar.title('Agregando tarea...')
    ventana_agregar.focus()

    label_ingresar_fecha = tkinter.Label(ventana_agregar, text='Ingrese la fecha (dd-mm-yyyy): ', font=fuente_tarea)
    label_ingresar_nombre = tkinter.Label(ventana_agregar, text='Ingrese el nombre: ', font=fuente_tarea)
    label_ingresar_descripcion = tkinter.Label(ventana_agregar, text='Agregue una breve descripción: ', font=fuente_tarea)
    entry_ingresar_fecha = tkinter.Entry(ventana_agregar, justify=tkinter.CENTER, font=fuente_tarea)
    entry_ingresar_nombre = tkinter.Entry(ventana_agregar, justify=tkinter.CENTER, font=fuente_tarea)
    entry_ingresar_descripcion = tkinter.Entry(ventana_agregar, justify=tkinter.CENTER, font=fuente_tarea)

    label_ingresar_fecha.grid(row=1, column=1, pady='10', padx='10')
    label_ingresar_nombre.grid(row=2, column=1, pady='5', padx='10')
    label_ingresar_descripcion.grid(row=3, column=1, pady='5', padx='10')
    entry_ingresar_fecha.grid(row=1, column=2, pady='10')
    entry_ingresar_nombre.grid(row=2, column=2, pady='5')
    entry_ingresar_descripcion.grid(row=3, column=2, pady='5')

# ------------------------------------------------------------------------------------------------
    import datetime

    def guardar_tarea():
        datos_tarea = []
        datos_tarea.append(entry_ingresar_fecha.get()), datos_tarea.append(entry_ingresar_nombre.get()), datos_tarea.append(entry_ingresar_descripcion.get())
        validar_fecha = str(datos_tarea[0])
        fecha_validada = ''
        fecha_mayor_validada = ''
        nombre_validado = ''
        descripcion_validada = ''
        format = "%d-%m-%Y"
        try: 
            bool(datetime.datetime.strptime(validar_fecha, format))
            fecha_validada = True
        except ValueError:
            messagebox.showerror('Error de formato', 'El formato de la fecha no es valido')
            ventana_agregar.focus()
        datos_listos_guardar = '|'
        datos_listos_guardar = datos_listos_guardar.join(datos_tarea)

        if fecha_validada:
            dia_validar = (int(datos_tarea[0][0:2])+1)
            mes_validar = int(datos_tarea[0][3:5])
            anio_validar = int(datos_tarea[0][6:10])
            fecha_datetime = datetime.datetime(anio_validar, mes_validar, dia_validar)
            if fecha_datetime>obtener_fecha:
                fecha_mayor_validada = True
            else:
                messagebox.showerror('Error de formato', '¡La fecha de la tarea ya paso!')
                ventana_agregar.focus()

        if len(str(datos_tarea[1])) > 1:
            nombre_validado = True
        else:
            messagebox.showerror('Error de formato', '¡El nombre de la tarea es muy corto!')
            ventana_agregar.focus()

        if len(str(datos_tarea[2])) > 1:
            descripcion_validada = True
        else:
            messagebox.showerror('Error de formato', '¡La descripcion de la tarea es muy corta!')
            ventana_agregar.focus()

        if fecha_validada == True and nombre_validado == True and descripcion_validada == True and fecha_mayor_validada == True:
            with open (r'preferences\tareas_usuario.txt', 'a') as archivo_datos:
                archivo_datos.write(datos_listos_guardar)
                archivo_datos.write('\n')
            ventana_agregar.destroy()
            main_window.focus()

    boton_cancelar_tarea = tkinter.Button(ventana_agregar, text= 'CANCELAR', relief='raised', overrelief='flat', font=fuente_tarea, command=lambda: ventana_agregar.destroy())
    boton_agregar_tarea = tkinter.Button(ventana_agregar, text= 'CONFIRMAR', relief='raised', overrelief='flat', font=fuente_tarea, fg='white', bg=color_adaptable, command=lambda:guardar_tarea())
    boton_agregar_tarea.grid(row=4, column=1, pady='10')
    boton_cancelar_tarea.grid(row=4, column=2, pady='10')   

boton_agregar_tarea = tkinter.Button(frame_top, text= 'AGREGAR TAREA', font=fuente_tarea, fg='white', bg=color_adaptable, command=generar_ventana_agregar_tarea)
boton_agregar_tarea.place(x=int(ancho*0.71), y=int(alto*0.21))

#----------------------------------------------------------------------

with open (r'preferences\tareas_usuario.txt', 'r') as archivo_tareas:
    tareas_leidas = [linea.strip() for linea in archivo_tareas]

tareas_separadas = []
for item in tareas_leidas:
    string_crudo = item.split("|")
    tareas_separadas.append(string_crudo)

#----------------------------------------------------------------------

nombre_usuario = user_preferences.get_nombre()

saludo = ('Bienvenido/a '+ nombre_usuario + '. La fecha es ' + fecha + '.')

label_bienvenida_tareas = tkinter.Label(frame_top, text=saludo, font=fuente_bienvenida, bg='white')
label_bienvenida_tareas.place(x=int(ancho*0.03), y=int(alto*0.215))

# frame_mes = tkinter.Frame(frame_top, bg='grey')
configurar_frame_top = ConfigurarFrame(frame_mes, 82,48)
frame_mes.place(x=int(ancho*0.028), y=int(alto*0.27))

# lista_meses = [0, 'Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre']
mes_obtenido = int(obtener_fecha.strftime('%m'))
mes_actual = int(mes_obtenido)
anio_actual = int(obtener_fecha.strftime('%Y'))
mes_string = lista_meses[mes_actual] + ' '+ str(anio_actual)

mes_variable_int = tkinter.IntVar(value=mes_actual)
anio_variable_int = tkinter.IntVar(value=anio_actual)
# mes_variable = tkinter.StringVar(frame_mes, value=mes_string)

label_mes_pantalla = tkinter.Label(frame_mes, textvariable=mes_variable, font=fuente_bienvenida, fg='white')
label_mes_pantalla.place(x=int(ancho*0.352), y=int(alto*0.02))

boton_mes_derecha.place(x=int(ancho*0.768), y=int(alto*0.2))
boton_mes_izquierda.place(x=int(ancho*0.008), y=int(alto*0.2))

def cambiar_mes(direccion):
    if direccion == 'Izquierda':
        mes_variable_int.set(mes_variable_int.get()-1)
        if (mes_variable_int.get()<1):
            mes_variable_int.set(12)
            anio_variable_int.set(anio_variable_int.get()-1)
        mes_string = lista_meses[mes_variable_int.get()] + ' '+ str(anio_variable_int.get())
        mes_variable.set(mes_string)
        
    elif direccion == 'Derecha':
        mes_variable_int.set(mes_variable_int.get()+1)
        if (mes_variable_int.get()>12):
            mes_variable_int.set(1)
            anio_variable_int.set(anio_variable_int.get()+1)
        mes_string = lista_meses[mes_variable_int.get()] + ' ' + str(anio_variable_int.get())
        mes_variable.set(mes_string)
        
print(mes_variable_int.get())
print(tareas_separadas)


#----------------------------------------------------------------------

def refrescar_clima():
    with open(r'preferences\ciudad_usuario.txt', 'r') as archivo_ciudad:
        ciudad_guardada = archivo_ciudad.readline()
        ciudad_guardada = ciudad_guardada+" clima"
    variable_ciudad_guardada.set(ciudad_guardada)
    print('Refrescando clima...')
    localidad_clima, tiempo_clima, info_clima, clima_grados = weather(variable_ciudad_guardada.get())
    variable_grados.set(clima_grados)
    variable_info.set(info_clima)
    variable_tiempo.set(tiempo_clima)
    variable_localidad.set(localidad_clima)
    frame_top.after(600000, refrescar_clima)

def refrescar_reloj():
    variable_hora.set(hora_completa())
    frame_top.after(1000, refrescar_reloj)

def refrescar_bg():
    horatk.set(hora_sola())
    frame_background.after(1000, refrescar_bg)
    frame_background.after(1000, background_adaptable)

#---------------------------------------------------------------------------------

refrescar_clima()
refrescar_reloj()
refrescar_bg()

main_window.mainloop()