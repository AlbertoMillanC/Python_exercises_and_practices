import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# Cargar los datos del archivo CSV
datos = pd.read_csv('datos_del_sorteo.csv')

# Dividir los datos en conjuntos de entrenamiento y prueba
x_entrenamiento, x_prueba, y_entrenamiento, y_prueba = train_test_split(
    datos.iloc[:, :-1], datos.iloc[:, -1], test_size=0.2, random_state=0)

# Crear y ajustar el modelo de regresión lineal
modelo = LinearRegression()
modelo.fit(x_entrenamiento, y_entrenamiento)

# Hacer una predicción en base a una serie de números anteriores
serie_anterior = [1, 2, 3, 4, 5, 6]
proximo_numero = modelo.predict([serie_anterior])[0]
