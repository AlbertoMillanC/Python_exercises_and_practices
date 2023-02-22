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
    datos.iloc[:-1], datos.iloc[1:], test_size=0.9, random_state=0)

# crear y ajustar el modelo de regresión lineal
modelo = LinearRegression()
modelo.fit(x_entrenamiento, y_entrenamiento)

# hacer una predicción en base a una serie de números anteriores
serie_anterior = datos.iloc[-1:, -4:].values.flatten().tolist()
proximo_numero = int(modelo.predict([serie_anterior])[0])

def test_load_data():
    assert datos is not None

def test_split_data():
    assert x_entrenamiento is not None
    assert x_prueba is not None
    assert y_entrenamiento is not None
    assert y_prueba is not None

def test_create_model():
    assert modelo is not None

def test_make_prediction():
    assert proximo_numero is not None
    
print(proximo_numero)

test_load_data()
test_split_data()
test_create_model()
test_make_prediction()
