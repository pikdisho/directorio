import tkinter
from PIL import ImageTk, Image

archivo_resolucion = open(r'Proyecto\preferences\resolucion_usuario.txt', 'r') # PARA LEER LA RESOLUCION GUARDADA
resolucion = archivo_resolucion.readline()
archivo_resolucion.close()

ancho = int(resolucion[0:4]) # PARA PODER REDIMENSIONAR EL TAMAñO DE LOS FRAMES E IMAGENES
alto = int(resolucion[5:9])

welcome = tkinter.Tk() #VENTANA PRINCIPAL
welcome.geometry(resolucion)
welcome.title('Pikwidget')
welcome.resizable(0,0)
# welcome.iconbitmap('wm', 'Proyecto\media\LOGO.png')

frameizquierda = tkinter.Frame(welcome, bg='blue')
frameizquierda.config(width=(ancho*0.66), height=(alto))
frameizquierda.pack(side=tkinter.LEFT, expand=1)

texto_redimensionada = Image.open('Proyecto\media\wlabel_cartelito.gif')
texto_redimensionada = texto_redimensionada.resize((int(ancho*0.34), int(alto/2)), Image.Resampling.LANCZOS)
textocartel = ImageTk.PhotoImage(texto_redimensionada)

imagen_redimensionada = Image.open('Proyecto\media\www.gif')
imagen_redimensionada = imagen_redimensionada.resize((int(ancho*0.66), alto), Image.Resampling.LANCZOS)
imagencartel = ImageTk.PhotoImage(imagen_redimensionada)

imagenlabel = tkinter.Label(frameizquierda, image=imagencartel)
imagenlabel.pack()

framederecha = tkinter.Frame(welcome)
framederecha.config(bg='white', width=(ancho*0.34), height=(alto))
framederecha.pack(side=tkinter.RIGHT, expand=1)
framederecha.pack_propagate(False)

texto_label = tkinter.Label(framederecha, image=textocartel)
texto_label.pack()

caja_nombre = tkinter.Entry(framederecha, justify=tkinter.CENTER, font='Gilroy 30', relief='solid')
caja_nombre.pack(anchor='center', padx=50, pady=30)

guardar_nombre = open(r'Proyecto\preferences\nombre_usuario.txt', 'w')

class nombre_user():
    nombre_introducido = ''
    def __init__(self):
        self.nombre_introducido = ''
    def set_nombre(self):
        self.nombre_introducido = caja_nombre.get()
        guardar_nombre.write(self.nombre_introducido)
        guardar_nombre.close()
        welcome.destroy()
    def get_nombre(self):
        return(self.nombre_introducido)
    
usuario = nombre_user() # CREAMOS EL OBJETO PARA PODER SETEAR EL NOMBRE

boton_siguiente= tkinter.Button(framederecha, text='CONTINUAR →', padx=50, pady=20, overrelief="flat", relief='groove', command=lambda: usuario.set_nombre())
boton_siguiente.pack()

welcome.mainloop()