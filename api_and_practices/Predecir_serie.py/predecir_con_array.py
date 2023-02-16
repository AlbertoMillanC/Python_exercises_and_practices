import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# Crear un array con 40 números para entrenamiento y otro con 20 para prueba
numeros = [i for i in range(000000, 999999) if len(set(str(i))) == 4]
numeros_entrenamiento = numeros[:9999]
numeros_prueba = numeros[2000:]

# Crear un DataFrame con los datos de los números
datos = pd.DataFrame({'Numero': numeros_entrenamiento})

# Añadir columnas para representar los 6 últimos números ganadores
for i in range(0, 6):
    datos[f'Ganador{i}'] = datos['Numero'].shift(i)

# Eliminar las filas quecontienen valores nulos
datos = datos.dropna()

# Dividir los datos en conjuntos de entrenamiento y prueba
x_entrenamiento, x_prueba, y_entrenamiento, y_prueba = train_test_split(
    datos.iloc[:, :-1], datos.iloc[:, -1], test_size=0.35, random_state=0)

# Crear y ajustar el modelo de regresión lineal
modelo = LinearRegression()
modelo.fit(x_entrenamiento, y_entrenamiento)

# Hacer una predicción en base a los 6 últimos números ganadores
serie_anterior = numeros_prueba[-6:]
proximo_numero = modelo.predict([serie_anterior])[0]
print(f'El próximo número ganador es: {int(proximo_numero)}')
