# Definir el número de átomos presentes y el peso atómico del elemento
num_atomos = 1.0e23
peso_atomico = 55.85  # peso atómico del hierro

# Calcular la masa de la muestra a partir del número de átomos y el peso atómico
masa = num_atomos * peso_atomico / 6.022e23

# Imprimir el resultado
print("La masa de la muestra es {:.2e} gramos".format(masa))
