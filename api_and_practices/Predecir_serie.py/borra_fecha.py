import csv

# Abrir archivo de entrada
with open("C:\\Users\\ASUS\\Desktop\\datos_del_sorteo.csv", "r") as f:
    reader = csv.reader(f)
    data = list(reader)

# Encontrar el índice de la columna "Fecha"
fecha_idx = data[0].index("Fecha")

# Eliminar la columna "Fecha" y sus datos
for row in data:
    del row[fecha_idx]

# Crear archivo de salida
with open("datos_del_sorteo_sin_fecha.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerows(data)

print("Proceso completado!")
