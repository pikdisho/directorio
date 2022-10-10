class import_user_data():    
    def __init__(self):
        with open(r'preferences\nombre_usuario.txt', 'r') as archivo_nombre:
            self.nombre = archivo_nombre.readline()
        with open(r'preferences\resolucion_usuario.txt', 'r') as archivo_resolucion:
            self.resolucion = archivo_resolucion.readline()
    def get_nombre(self):
        return(self.nombre)
    def get_resolucion(self):
        return(self.resolucion)
    def get_ancho_alto(self):
        ancho = int(self.resolucion[0:4]) # PARA PODER REDIMENSIONAR EL TAMAñO DE LOS FRAMES E IMAGENES
        alto = int(self.resolucion[5:9])
        return(ancho, alto)
    def set_main_window_preferences(self, ventana_a_configurar):
        ventana_a_configurar.geometry(self.get_resolucion())
        ventana_a_configurar.title('pikWidget')
        ventana_a_configurar.resizable(0,0)
        ventana_a_configurar.iconbitmap('wm', r'media\favicon.ico')

class ConfigurarFrame:
    def __init__(self, frame, porcentajealto, porcentajebajo):
        with open(r'preferences\resolucion_usuario.txt', 'r') as archivo_resolucion:
            resolucion = archivo_resolucion.readline()
        ancho = int(resolucion[0:4])
        alto = int(resolucion[5:9])
        frame.config(width=porcentajealto/100*ancho, height=porcentajebajo/100*alto)

