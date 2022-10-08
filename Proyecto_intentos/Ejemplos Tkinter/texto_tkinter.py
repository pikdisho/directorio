import tkinter as tk
import tkinter.font as tkFont

root = tk.Tk()
root.geometry("400x240")

textExample=tk.Text(root, height=10)
textExample.pack()

fontExample = tkFont.Font(family="Arial", size=16, weight="bold", slant="italic")

textExample.configure(font=fontExample)

root.mainloop()

# El constructor de fuentes tiene opciones como,

# family - familia de fuentes, como Arial, Courier.
# size - tamaño de la fuente (en puntos)
# weight - espesor, normal o bold
# slant - inclinación de la fuente: roman o italic
# underline - subrayado de la fuente, False o True
# overstrike - tachar la fuente, False o True.
# La ventaja de usar un objeto Font en lugar de un tipo de fuente tuple es que el mismo objeto Font puede ser asignado a diferentes widgets y puede ser actualizado programáticamente con el método Font.configure. Todos los widgets que tengan el mismo objeto font serán actualizados al nuevo estilo font.

# fontExample.configure(weight='normal')
# Actualiza el peso de fontExample para que sea normal.

# https://www.delftstack.com/es/howto/python-tkinter/how-to-create-a-tkinter-window-with-a-constant-size/