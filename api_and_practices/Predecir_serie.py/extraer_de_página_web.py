import requests
from bs4 import BeautifulSoup

url = 'https://www.astroluna.co/boyaca'

# Realizar una solicitud a la página web y obtener el HTML
response = requests.get(url)
html = response.content

# Parsear el HTML usando beautifulsoup
soup = BeautifulSoup(html, 'html.parser')

# Encontrar la tabla que contiene los números con el valor "numeros"
tabla_numeros = soup.find('table', {'id': 'numeros'})

# Extraer los números de la tabla
numeros = []
filas = tabla_numeros.find_all('tr')
for fila in filas:
    celdas = fila.find_all('td')
    if len(celdas) == 2 and celdas[1].text.strip() == "numeros":
        numeros.extend(celdas[0].text.strip().split(','))

print(numeros)
