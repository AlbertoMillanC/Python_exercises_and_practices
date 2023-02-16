import csv
import random

# Generar los datos aleatorios
datos = [[random.randint(1000, 9999)] for i in range(4000)]

# Escribir los datos en el archivo csv
with open('datos_del_sorteo.csv', 'w', newline='') as archivo:
    escritor_csv = csv.writer(archivo)
    escritor_csv.writerows(datos)
