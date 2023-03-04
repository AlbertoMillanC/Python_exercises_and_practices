# Definir la fórmula química del compuesto
formula = "C12H22O11"

# Definir las cantidades de cada elemento en la muestra
cantidad_c = 12
cantidad_h = 22
cantidad_o = 11

# Definir los pesos atómicos de cada elemento
peso_c = 12.01
peso_h = 1.01
peso_o = 16.00

# Calcular el número de átomos de cada elemento en la muestra
num_atoms_c = cantidad_c * (10 / peso_c) * 6.022e23
num_atoms_h = cantidad_h * (10 / peso_h) * 6.022e23
num_atoms_o = cantidad_o * (10 / peso_o) * 6.022e23

# Imprimir los resultados
print("Número de átomos de carbono en la muestra:", num_atoms_c)
print("Número de átomos de hidrógeno en la muestra:", num_atoms_h)
print("Número de átomos de oxígeno en la muestra:", num_atoms_o)
