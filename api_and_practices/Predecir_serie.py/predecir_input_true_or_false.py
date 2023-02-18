import numpy as np
import json
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# cargar los datos del archivo json
with open('datos_del_sorteo.json', 'r') as f:
    data = json.load(f)
datos = pd.DataFrame(data['numeros'])

# convertir los números en variables numéricas
datos = datos.apply(pd.to_numeric)

# dividir los datos en conjuntos de entrenamiento y prueba
x_entrenamiento, x_prueba, y_entrenamiento, y_prueba = train_test_split(
    datos.iloc[:-1], datos.iloc[1:], test_size=0.2, random_state=0)

# crear y ajustar el modelo de regresión lineal
modelo = LinearRegression()
modelo.fit(x_entrenamiento, y_entrenamiento)

# hacer una predicción en base a una serie de números anteriores
while True:
    serie_anterior = datos.iloc[-1:, -4:].values.flatten().tolist()
    proximo_numero = int(modelo.predict([serie_anterior])[0])
    print(f'La próxima predicción es: {proximo_numero}')
    respuesta = input('¿Es correcta la predicción? (s/n): ')
    if respuesta.lower() == 's':
        break

# Si la predicción es incorrecta, reajustar el modelo y hacer una nueva predicción
while respuesta.lower() == 'n':
    x_entrenamiento, x_prueba, y_entrenamiento, y_prueba = train_test_split(
        datos.iloc[:-1], datos.iloc[1:], test_size=0.2, random_state=0)
    modelo = LinearRegression()
    modelo.fit(x_entrenamiento, y_entrenamiento)
    serie_anterior = datos.iloc[-1:, -4:].values.flatten().tolist()
    proximo_numero = int(modelo.predict([serie_anterior])[0])
    print(f'La próxima predicción es: {proximo_numero}')
    respuesta = input('¿Es correcta la predicción? (s/n): ')
    
