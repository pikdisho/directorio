import tkinter as tk

class MainWindow:
    # Le pasamos el componente raíz al constructor
    def __init__(self, root):
        # Establecemos el tamaño de la raíz
        root.geometry("100x50")
        # Añadimos el botón y lo empaquetamos
        button = tk.Button(root, text="Hola", command=self.hola)
        button.pack()

    # Definimos la función como un método de clase
    def hola(self):
        print("¡Hola mundo!")


# Creamos la aplicación, la ventana e iniciamos el bucle
app = tk.Tk()
window = MainWindow(app)
app.mainloop()