# Abrir archivo de entrada
with open("C:\\Users\\ASUS\\Desktop\\datos_del_sorteo.csv", "r") as f:
    data = f.read()

# Quitar espacios
data = data.replace(" ", " ")

# Crear archivo de salida
with open("C:\\Users\\ASUS\\Desktop\\datos_del_sorteo_comas.csv", "w") as f:
    f.write(data.replace("\n", ","))

print("Proceso completado!")
