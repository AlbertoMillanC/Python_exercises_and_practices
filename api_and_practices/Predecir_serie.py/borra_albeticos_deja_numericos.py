import re

# Abrir archivo de entrada
with open("C:\\Users\\ASUS\\Desktop\\datos_del_sorteo.csv", "r") as f:
    data = f.read()

# Buscar solo los valores numéricos y unirlos con comas
data = ",".join(re.findall(r"\d+", data))

# Crear archivo de salida
with open("C:\\Users\\ASUS\\Desktop\\datos_del_sorteo_comas.csv", "w") as f:
    f.write(data)

print("Proceso completado!")
