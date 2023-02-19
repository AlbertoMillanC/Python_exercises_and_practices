import json
import pandas as pd
import numpy as np
from sklearn.neural_network import MLPRegressor

# Cargar el archivo JSON y convertirlo a un dataframe
with open('api_and_practices/Predecir_serie.py/predecir_redes_neuronales/numeros_ganadores.json') as f:
    data = json.load(f)

df = pd.DataFrame(data)

# Seleccionar las columnas de interés
X = df[['Num1', 'Num2', 'Num3', 'Num4']]
y = df['Jackpot']

# Crear un modelo de red neuronal y ajustarlo a los datos
model = MLPRegressor(hidden_layer_sizes=(20, 5,20, 5,20, 5,20, 5,20, 5,20, 5,20, 5,20, 5,20, 5,20, 5,20, 5,20, 5,20, 5, 10, 10, 10), max_iter=100000000)
model.fit(X, y)

# Predecir el valor del jackpot para un nuevo conjunto de números ganadores
nuevos_numeros = [[9, 2, 0, 0]]
prediccion = model.predict(nuevos_numeros)
prediccion = np.clip(prediccion, 0000, 9999)



print("La predicción para los números ganadores es:", int(prediccion))
