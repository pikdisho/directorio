import tkinter
from resolucion_win import *

resolucion = '1920x1080'
ancho = int(resolucion[0:4])
alto = int(resolucion[5:9])

welcome = tkinter.Tk()
welcome.geometry(resolucion)
welcome.title('Pikwidget')

cartel = tkinter.Frame(welcome)
cartel.config(bg='blue', width=(ancho/2), height=(alto))
cartel.grid(row=0, column=0)

imagencartel = tkinter.PhotoImage(file='Proyecto\media\TEXTOPNGPRUEBA.png')
imagenlabel = tkinter.Label(cartel, image=imagencartel)
imagenlabel.config(width='500', height='217')
imagenlabel.place(x=0, y=0)

cartel2 = tkinter.Frame(welcome)
cartel2.grid(row=0, column=1)

caja_nombre = tkinter.Entry(cartel2)
caja_nombre.pack()

welcome.mainloop()