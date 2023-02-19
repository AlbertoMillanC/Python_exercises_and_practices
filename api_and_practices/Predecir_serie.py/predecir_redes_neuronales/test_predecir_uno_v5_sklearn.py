import json
import pandas as pd
from sklearn.linear_model import LinearRegression

# Cargar el archivo JSON y convertirlo a un dataframe
with open('api_and_practices/Predecir_serie.py/predecir_redes_neuronales/numeros_ganadores.json') as f:
    data = json.load(f)

df = pd.DataFrame(data)

# Seleccionar las columnas de interés
X = df[['Num1', 'Num2', 'Num3', 'Num4', 'Num5', 'Powerball']]
y = df['Jackpot']

# Crear un modelo de regresión lineal y ajustarlo a los datos
model = LinearRegression()
model.fit(X, y)

# Predecir el valor del jackpot para un nuevo conjunto de números ganadores
nuevos_numeros = [[12, 34, 45, 51, 67, 5]]
prediccion = model.predict(nuevos_numeros)

print("La predicción para los números ganadores es:", prediccion)
