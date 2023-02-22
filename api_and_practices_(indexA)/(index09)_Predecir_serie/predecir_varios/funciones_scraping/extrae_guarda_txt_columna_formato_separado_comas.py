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

# Extraer los datos de la tabla
datos = []
filas = tabla.find_all('tr')
for fila in filas:
    celdas = fila.find_all('td')
    fila_datos = [celda.text.strip() for celda in celdas]
    # eliminar la primera y última columna
    del fila_datos[0]
    del fila_datos[-1]
    datos.append(fila_datos)

# Guardar los datos en un archivo de texto separado por comas
with open('datos_boyaca.csv', 'w') as archivo_csv:
    for fila_datos in datos:
        archivo_csv.write(','.join(fila_datos) + '\n')

print(f"Los datos se han guardado en {archivo_csv.name}")
