import tkinter

selector = tkinter.Tk()
selector.title('pikWidget')
selector.geometry('300x60')
selector.wm_resizable(0,0)
selector.iconbitmap('wm', r'media\favicon.ico')

guardar_resolucion = open(r'preferences\resolucion_usuario.txt', 'w')

class resoluciones_posibles():
    def __init__(self):
        self.resolucion = None

    def set_resolucion(self, resolucion_apretada):
        self.resolucion = resolucion_apretada
        guardar_resolucion.write(resolucion_apretada)
        guardar_resolucion.close()
        selector.destroy()

resolucion_seleccionada = resoluciones_posibles()

cartel = tkinter.Label(selector, text='SELECCIONA LA RESOLUCION')
cartel.grid(row=0, column=1)

boton1080 = tkinter.Button(selector, text='1920x1080', overrelief="flat", command=lambda: resolucion_seleccionada.set_resolucion('1920x1080'))
boton1080.grid(row=1, column=0)

boton766 = tkinter.Button(selector, text='1366x768', overrelief="flat", command=lambda: resolucion_seleccionada.set_resolucion('1366x768'))
boton766.grid(row=1, column=1)

boton720 = tkinter.Button(selector, text='1280x720', overrelief="flat", command=lambda: resolucion_seleccionada.set_resolucion('1280x720'))
boton720.grid(row=1, column=2)

selector.mainloop()