import requests
from bs4 import BeautifulSoup
from tabulate import tabulate

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

# Guardar los datos en un archivo de texto en formato tabla
with open('datos_boyaca.txt', 'w') as archivo_txt:
    archivo_txt.write(tabulate(datos, headers=cabecera, tablefmt='psql'))

print(f"Los datos se han guardado en {archivo_txt.name}")





# Eliminar la primera columna de la lista de datos (columna "fecha")
datos_sin_fecha = [fila[1:] for fila in datos]

# Guardar los datos en un archivo de texto en formato tabla
with open('datos_boyaca.txt', 'w') as archivo_txt:
    archivo_txt.write(tabulate(datos_sin_fecha, headers=cabecera[1:], tablefmt='psql'))

print(f"Los datos se han guardado en {archivo_txt.name}")

