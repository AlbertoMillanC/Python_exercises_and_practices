import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

def test_load_data():
    # cargar los datos del archivo de texto
    datos = pd.read_csv('datos_del_sorteo_comas.csv', delimiter=',')
    assert datos is not None

def test_split_data():
    # cargar los datos del archivo de texto
    datos = pd.read_csv('datos_del_sorteo_comas.csv', delimiter=',')

    # dividir los datos en conjuntos de entrenamiento y prueba
    x_entrenamiento, x_prueba, y_entrenamiento, y_prueba = train_test_split(
        datos.iloc[:, :-1], datos.iloc[:, -1], test_size=0.2, random_state=0)

    assert x_entrenamiento is not None
    assert x_prueba is not None
    assert y_entrenamiento is not None
    assert y_prueba is not None

def test_create_model():
    # cargar los datos del archivo de texto
    datos = pd.read_csv('datos_del_sorteo_comas.csv', delimiter=',')

    # dividir los datos en conjuntos de entrenamiento y prueba
    x_entrenamiento, x_prueba, y_entrenamiento, y_prueba = train_test_split(
        datos.iloc[:, :-1], datos.iloc[:, -1], test_size=0.2, random_state=0)

    # crear y ajustar el modelo de regresión lineal
    modelo = LinearRegression()
    modelo.fit(x_entrenamiento, y_entrenamiento)

    assert modelo is not None

def test_make_prediction():
    # cargar los datos del archivo de texto
    datos = pd.read_csv('datos_del_sorteo_comas.csv', delimiter=',')

    # dividir los datos en conjuntos de entrenamiento y prueba
    x_entrenamiento, x_prueba, y_entrenamiento, y_prueba = train_test_split(
        datos.iloc[:, :-1], datos.iloc[:, -1], test_size=0.2, random_state=0)

    # crear y ajustar el modelo de regresión lineal
    modelo = LinearRegression()
    modelo.fit(x_entrenamiento, y_entrenamiento)

    # hacer una predicción en base a una serie de números anteriores
    serie_anterior = [1000, 2000, 3000, 4000]
    proximo_numero = modelo.predict([serie_anterior])[0]

    assert proximo_numero is not None

test_load_data()
test_split_data()
test_create_model()
test_make_prediction()
