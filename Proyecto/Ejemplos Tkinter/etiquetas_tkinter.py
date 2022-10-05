import tkinter

interfaz = tkinter.Tk()
interfaz.geometry('720x360')

etiqueta1 = tkinter.Label(interfaz, text= 'Olaaaa gente', bg='GREEN')
etiqueta1.pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=True) # FILL ES PARA RELLENAR, PUEDE SER X, Y O BOTH PARA RELLENAR TODO EL WIDGET

etiqueta2 = tkinter.Label(interfaz, text= 'Estoy abajo genteeeeeeeeeee')
etiqueta2.pack(side=tkinter.BOTTOM) #RIGHT, LEFT, ETC

etiqueta3 = tkinter.Label(interfaz, text='Probandooooooooooooooooooo', bg='red')
etiqueta3.pack(side=tkinter.LEFT, expand=False) #Cuando le damos con config un tamañp predeterminado, con expand podemos permitir que el widget se ajuste a la ventana o no
etiqueta3.config(width='50', height='50')

interfaz.mainloop()