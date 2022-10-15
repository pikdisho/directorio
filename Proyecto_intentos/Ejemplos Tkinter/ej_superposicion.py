import tkinter as tk

ventana = tk.Tk()
ventana.geometry("300x400")
frame_rojo = tk.Frame(ventana, bg="red")
frame_verde = tk.Frame(ventana, bg="green")
frame_azul = tk.Frame(ventana, bg="blue")
frame_rojo.place(x=50, y=50, height=200, width=200)
frame_verde.place(x=70, y=70, height=200, width=200)
frame_azul.place(x=90, y=90, height=200, width=200)

tk.Button(ventana, text="Rojo  arriba", command=frame_rojo.lift).place(x=100, y=300)
tk.Button(ventana, text="Rojo   abajo", command=frame_rojo.lower).place(x=100, y=350)

ventana.mainloop()