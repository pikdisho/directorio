import tkinter

selector = tkinter.Tk()
selector.title('Pikwidget')
selector.geometry('480x100')
selector.wm_resizable(0,0)

cartel = tkinter.Label(selector, text='SELECCIONA LA RESOLUCION')
# cartel.pack(side=tkinter.TOP, fill = tkinter.X)
cartel.grid(row=0, column=1)

def resolucionelegida(resolucion):
    print(resolucion)
    return(resolucion)

boton1080 = tkinter.Button(selector, text='1920x1080', command=lambda: resolucionelegida('1920x1080'))
boton1080.grid(row=1, column=0)

boton766 = tkinter.Button(selector, text='1366x768', command=lambda: resolucionelegida('1366x768'))
boton766.grid(row=1, column=1)

boton720 = tkinter.Button(selector, text='1280x720', command=lambda: resolucionelegida('1280x720'))
boton720.grid(row=1, column=2)

selector.mainloop()

# while True:
#     selector.mainloop()
#     if len()>0:
#         selector.destroy()
#         break
    
    