import ctypes

user32 = ctypes.windll.user32
user32.SetProcessDPIAware()
ancho, alto = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)

def resolucion():   
    resolucion_pantalla = str(ancho) + "x" + str(alto)
    return(resolucion_pantalla)
