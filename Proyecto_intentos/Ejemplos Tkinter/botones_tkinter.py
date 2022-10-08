import tkinter

interfaz = tkinter.Tk()
interfaz.geometry('720x360')

def saludoaparabotoncito():
    print('Apretaste el boton OMG')

def botoncitoconparametros(parametrooo):
    print('Holaaaaaaaaaaa', parametrooo)

botoncito = tkinter.Button(interfaz, text='PRESIONE AKI', padx=30, pady=20, command=saludoaparabotoncito) #NUNCA PONER PARENTESIS PARA INCIAR UNA FUNCION
botoncito.pack()

botoncitoavanzado = tkinter.Button(interfaz, text='Presione para ejecutar boton avanzado', command=lambda: botoncitoconparametros('Franco')) #ALTERNATIVA DENTRO DE LAMBDA PUEDO DEFINIR UN PRINT SIN DECLARARLO ANTES
#LAMBDA FUNCIONA PARA DEFINIR FUNCIONES EN LA MISMA LINEA, PARA USAR FUNCIONES CON PARAMETROS, FUNCIONES MUY CORTA A UTILZAR UNA SOLA VEZ
# ej        botoncitoavanzado = tkinter.Button(interfaz, text='Presione', command=lambda: print('Holaaaaaaaaaa))
botoncitoavanzado.pack(side=tkinter.BOTTOM)


interfaz.mainloop()