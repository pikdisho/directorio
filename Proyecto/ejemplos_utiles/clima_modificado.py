from bs4 import BeautifulSoup
import requests
from time import sleep
headers = {
	'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}


def weather(city):
	# city = city.replace(" ", "+")
	page_concatenada = 'https://www.https://www.clima.com/argentina/salta/salta'
	print(page_concatenada)
	page_clima = requests.get(page_concatenada)

	print("Searching...\n")
	sleep(3)
	soup = BeautifulSoup(page_clima.text, 'html.parser')
	# location = soup.select('#wob_loc')[0].getText().strip()
	# time = soup.select('#wob_dts')[0].getText().strip()
	# info = soup.select('#wob_dc')[0].getText().strip()
	maximo = soup.select("#data-temp")[0].get_text().strip()
	# weather = soup.select('#wob_tm')[0].getText().strip()
	# print(location)
	# print(time)
	# print(info)
	# print(weather+"°C")
	print(maximo)

city = input("Enter the Name of City -> ")
city = city+" weather"
weather(city)
print("Have a Nice Day:)")

# This code is contributed by adityatri
