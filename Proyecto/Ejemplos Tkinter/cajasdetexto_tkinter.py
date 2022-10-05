import tkinter

interfaz = tkinter.Tk()
interfaz.geometry('720x360')

cajadetexto = tkinter.Entry(interfaz, font='Arial 16')
cajadetexto.pack()

etiketa = tkinter.Label(interfaz)
etiketa.pack()

def guardartextodelacaja():
    textoguardado = cajadetexto.get()
    etiketa['text'] = textoguardado
    print(textoguardado)

botonparacaja = tkinter.Button(interfaz, text='Hace click', command=guardartextodelacaja)
botonparacaja.pack()


interfaz.mainloop()