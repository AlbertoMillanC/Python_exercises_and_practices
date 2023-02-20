import csv
import requests
from bs4 import BeautifulSoup
from prettytable import from_csv

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

# Extraer los nombres de las columnas
cabecera = [th.text for th in tabla.find('thead').find_all('th')]

# Extraer los datos de la tabla
datos = []
filas = tabla.find_all('tr')
for fila in filas:
    celdas = fila.find_all('td')
    fila_datos = []
    for celda in celdas:
        fila_datos.append(celda.text.strip())
    datos.append(fila_datos)

# Guardar los datos en un archivo CSV
with open('datos_boyaca.csv', mode='w', newline='') as archivo_csv:
    writer = csv.writer(archivo_csv, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    writer.writerow(cabecera)
    for fila in datos:
        writer.writerow(fila)

# Leer el archivo CSV y convertirlo en una tabla
with open('datos_boyaca.csv', 'r') as archivo_csv:
    tabla_csv = from_csv(archivo_csv)

# Imprimir la tabla
print(tabla_csv)

print(f"Los datos se han guardado en {archivo_csv.name}")
