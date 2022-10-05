import tkinter

interfaz = tkinter.Tk()
interfaz.geometry('720x360')

boton1 = tkinter.Button(interfaz, text='Presione aki 1', width='10', height='5')
boton2 = tkinter.Button(interfaz, text='Presione aki 2', width='10', height='5')
boton3 = tkinter.Button(interfaz, text='Presione aki 3', width='10', height='5')

boton1.grid(row=0, column=0)
boton2.grid(row=1, column=1)
boton3.grid(row=4, column=4)

interfaz.mainloop()