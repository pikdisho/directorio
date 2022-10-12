from datetime import date, time, datetime
def hora_completa():
    return datetime.now().strftime('%H:%M:%S')
def hora_sola():
    return (int(datetime.now().strftime('%H')))
def segundero():
    return (int(datetime.now().strftime('%S')))

hora_tiempo_del_dia = hora_sola()
def tiempo_del_dia():
    if (hora_tiempo_del_dia >= 6 and hora_tiempo_del_dia < 13):
        return('maniana')
    if (hora_tiempo_del_dia >= 13 and hora_tiempo_del_dia < 20):
        return('tarde')
    if ((hora_tiempo_del_dia >= 20 and hora_tiempo_del_dia < 25) or (hora_tiempo_del_dia >= 0 and hora_tiempo_del_dia < 6)):
        return('noche')

from bs4 import BeautifulSoup
import requests
headers = {
	'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}

with open('preferences\ciudad_usuario.txt', 'r') as archivo_ciudad:
    ciudad_guardada = archivo_ciudad.readline()
ciudad_guardada = ciudad_guardada+" clima"

def weather(ciudad):
	ciudad = ciudad.replace(" ", "+")
	pagina = requests.get(
		f'https://www.google.com/search?q={ciudad}&oq={ciudad}&aqs=chrome.0.35i39l2j0l4j46j69i60.6128j1j7&sourceid=chrome&ie=UTF-8', headers=headers)
	# print("Searching...\n")
	soup = BeautifulSoup(pagina.text, 'html.parser')
	location = soup.select('#wob_loc')[0].getText().strip()
	time = soup.select('#wob_dts')[0].getText().strip()
	info = soup.select('#wob_dc')[0].getText().strip()
	weather = soup.select('#wob_tm')[0].getText().strip()
	print(location, time, info, weather+"°C")
	return(location, time, info, weather+"°C")

