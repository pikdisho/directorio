import tkinter
from resolucion_win import *
from UI_selector_resolucion import resolucion_seleccionada

resolucion = resolucion_seleccionada.resolucion
ancho = int(resolucion[0:4])
alto = int(resolucion[5:9])

welcome = tkinter.Tk()
welcome.geometry(resolucion_seleccionada.resolucion)
welcome.title('Pikwidget')

cartel = tkinter.Frame(welcome)
cartel.config(width=(ancho/2), height=(alto))
cartel.grid(row=0, column=0)

imagencartel = tkinter.PhotoImage(file='Proyecto\media\welcomebg.png')
# canvascartel = tkinter.Canvas(cartel, width=500, height=217)

# canvascartel.place(x=0, y=0)
# canvascartel.create_image( 0, 0, image = imagencartel,  
#                      anchor = "nw")


imagenlabel = tkinter.Label(cartel, image=imagencartel)
# imagenlabel.config(width='960', height='1080')
# imagenlabel.pack(cartel, fill=tkinter.BOTH, expand=True)
imagenlabel.place(x=-5, y=-40)

cartel2 = tkinter.Frame(welcome)
cartel2.config(bg='cyan', width=(ancho/2), height=(alto))
cartel2.grid(row=0, column=1)

# caja_nombre = tkinter.Entry(cartel2)
# caja_nombre.pack()

welcome.mainloop()