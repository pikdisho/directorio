lista_evento_nuevo = []

def asignar_numero():
    cantidad_lineas = 0
    with open(r'ejemplos_utiles\fichero.txt', 'r') as archivo_para_contar:
        contenido_crudo = archivo_para_contar.read()
        contenido = contenido_crudo.split('\n')
        for i in contenido:
            cantidad_lineas+=1
    return(cantidad_lineas)


def evento_nuevo():
    asignar_numero_evento = lista_evento_nuevo.append(str(asignar_numero()))
    nombre_evento = input('1: ')
    lista_evento_nuevo.append(nombre_evento)
    dia_evento = input('2: ')
    lista_evento_nuevo.append(dia_evento)
    descripcion_evento = input('3: ')
    lista_evento_nuevo.append(descripcion_evento)

    evento_string_total = '|'
    evento_string_total = evento_string_total.join(lista_evento_nuevo)
    print(lista_evento_nuevo)
    print(evento_string_total)
    with open(r'ejemplos_utiles\fichero.txt', 'a') as archivo_para_guardar_nuevo_evento:
        archivo_para_guardar_nuevo_evento.write(evento_string_total)
        archivo_para_guardar_nuevo_evento.write('\n')


lista_eventos_totales = []

evento_nuevo()
