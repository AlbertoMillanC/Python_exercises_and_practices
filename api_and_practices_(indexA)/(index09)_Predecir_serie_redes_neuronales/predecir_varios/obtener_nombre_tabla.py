import requests
from bs4 import BeautifulSoup

url = 'https://www.astroluna.co/boyaca'

# Realizar una solicitud a la página web y obtener el HTML
response = requests.get(url)
if response.status_code == 200:
    print("Conexión exitosa")
else:
    print("Error al conectarse a la página web")
    exit()

html = response.content

# Parsear el HTML usando beautifulsoup
soup = BeautifulSoup(html, 'html.parser')

# Encontrar la tabla que contiene los números
tabla = soup.find('table', {'id': 'tabla-resultados'})

# Obtener el nombre de la tabla
nombre_tabla = tabla['id']

# Obtener los nombres de las columnas
columnas = []
cabecera = tabla.find('thead')
filas = cabecera.find_all('tr')
for fila in filas:
    celdas = fila.find_all('th')
    for celda in celdas:
        columnas.append(celda.text)

print("Nombre de la tabla:", nombre_tabla)
print("Nombres de las columnas:", columnas)
