import tkinter as tk

class MainWindow:
    # Le pasamos el componente raíz al constructor
    def __init__(self, root):
        # Establecemos el tamaño de la raíz
        root.geometry("1920x1080")
        # Añadimos el botón y lo empaquetamos
        button = tk.Button(root, text="Hola", command=self.hola)
        button.pack()

    # Definimos la función como un método de clase
    def hola(self):
        print("¡Hola mundo!")

class ConfigurarFrame:
    # Le pasamos el componente raíz al constructor
    def __init__(self, frame, porcentajealto, porcentajebajo):
        # Establecemos el tamaño de la raíz
        frame.config(width=porcentajealto/100*1920, height=porcentajebajo/100*1080)


# Creamos la aplicación, la ventana e iniciamos el bucle
app = tk.Tk()
frame1=tk.Frame(app)
frameporcentaje = ConfigurarFrame(frame1,50,50)
frame1.config(bg = 'blue')
frame1.pack()
window = MainWindow(app)
app.mainloop()