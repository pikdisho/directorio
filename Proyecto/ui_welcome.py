import tkinter
from resolucion_win import *

resolucion = resolucion()
ancho = int(resolucion[3:5])
print(ancho)

welcome = tkinter.Tk()
welcome.geometry(resolucion)

cartel = tkinter.Frame(welcome)
cartel.config(bg='blue')
cartel.grid(row=0, column=0)

cartel2 = tkinter.Frame(welcome)
cartel2.grid(row=0, column=1)



welcome.mainloop()