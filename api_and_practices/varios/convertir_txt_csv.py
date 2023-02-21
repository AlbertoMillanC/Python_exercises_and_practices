import csv

with open('datos_red_grupos8.txt', 'r') as archivo_txt:
    contenido_txt = csv.reader(archivo_txt, delimiter=',')

    with open('datos_red_grupos8.csv', 'w', newline='') as archivo_csv:
        writer = csv.writer(archivo_csv)
        writer.writerows(contenido_txt)
