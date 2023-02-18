# Abrir archivo de entrada
with open("datos_boyaca.txt", "r") as f:
    data = f.read()

# Quitar espacios
data = data.replace(" ", " ")

# Crear archivo de salida
with open("C:\\Users\\ASUS\\Desktop\\datos_del_sorteo_comas.txt", "w") as f:
    f.write(data.replace("\n", ","))

print("Proceso completado!")
