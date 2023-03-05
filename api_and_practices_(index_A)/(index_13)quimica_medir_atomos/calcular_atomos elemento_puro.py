import numpy as np
from scipy.constants import Avogadro

# Definir el peso atómico del elemento y la cantidad de sustancia presente
peso_atomico = 55.85  # peso atómico del hierro
cantidad_sustancia = 1.0  # cantidad de sustancia en moles

# Calcular el número de átomos a partir del peso atómico y la cantidad de sustancia
masa_molar = peso_atomico / Avogadro  # calcular la masa molar del elemento
masa = cantidad_sustancia * masa_molar  # calcular la masa de la muestra
num_atomos = np.round(cantidad_sustancia * Avogadro)  # calcular el número de átomos

# Imprimir los resultados
print("Masa de la muestra: {:.2f} gramos".format(masa))
print("Número de átomos en la muestra: {:.2e} átomos".format(num_atomos))
