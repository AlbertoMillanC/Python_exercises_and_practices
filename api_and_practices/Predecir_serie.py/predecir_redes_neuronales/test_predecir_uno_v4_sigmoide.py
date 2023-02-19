import json
import random
import numpy as np
from keras.models import Sequential
from keras.layers import LSTM, Dense
from datetime import datetime


def guardar_prediccion(prediccion):
    fecha_hora = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    prediccion_str = str(round(prediccion[0][0]))
    with open('numeros_ganadores.json', 'r') as f:
        data = json.load(f)
    predicciones = data.get('predicciones', [])
    predicciones.append(
        {'fecha_hora': fecha_hora, 'prediccion model v4': prediccion_str})
    with open('numeros_ganadores.json', 'w') as f:
        json.dump({'predicciones': predicciones}, f, indent=4)


# Cargar datos del archivo JSON
with open('api_and_practices/Predecir_serie.py/predecir_redes_neuronales/numeros_ganadores.json') as f:
    data = json.load(f)

# Preprocesar los datos
numeros = [int(x) for x in data['numeros']]
secuencia_longitud = 60  # la longitud de la secuencia de entrada
X = []
y = []
for i in range(len(numeros) - secuencia_longitud):
    secuencia = numeros[i:i+secuencia_longitud]
    objetivo = numeros[i+secuencia_longitud]
    X.append(secuencia)
    y.append(objetivo)

# Convertir los datos a matrices numpy
X = np.reshape(X, (len(X), secuencia_longitud, 1))
X = X / float(9999)
y = np.array(y)
y = y / float(9999)

# Crear el modelo de RNN
modelo = Sequential()
modelo.add(LSTM(32, input_shape=(X.shape[1], X.shape[2])))
modelo.add(Dense(1, activation='sigmoid'))

# Compilar el modelo
modelo.compile(loss='mean_squared_error',
               optimizer='adam', metrics=['accuracy'])

# Definir el límite máximo de épocas y el valor objetivo
max_epochs = 10
target_score = 9200

# Separar datos de entrenamiento y validación
total_datos = len(X)
idx_entrenamiento = random.sample(range(total_datos), int(total_datos*0.8))
idx_validacion = [idx for idx in range(
    total_datos) if idx not in idx_entrenamiento]

X_entrenamiento, y_entrenamiento = X[idx_entrenamiento], y[idx_entrenamiento]
X_validacion, y_validacion = X[idx_validacion], y[idx_validacion]

# Entrenar el modelo
for i in range(max_epochs):
    modelo.fit(X_entrenamiento, y_entrenamiento, epochs=100, batch_size=100,
               verbose=2, validation_data=(X_validacion, y_validacion))
    puntuacion_entrenamiento = modelo.evaluate(
        X_entrenamiento, y_entrenamiento, verbose=3)
    puntuacion_validacion = modelo.evaluate(
        X_validacion, y_validacion, verbose=1)
    print('Precisión del modelo en la época {}: entrenamiento = {}, validación = {}'.format(
        i, puntuacion_entrenamiento[1], puntuacion_validacion[1]))
    if puntuacion_validacion[1]*100 >= target_score:
        print('Se ha alcanzado la precisión objetivo en la época {}'.format(i))
        # Guardar los parámetros en un archivo de texto
        with open('parametros.txt', 'w') as f:
            f.write('Época: {}\n'.format(i))
            f.write('Precisión de entrenamiento: {}\n'.format(puntuacion_entrenamiento[1]))
            f.write('Precisión de validación: {}\n'.format(puntuacion_validacion[1]))
        # Guardar los pesos del modelo en un archivo
        modelo.save_weights('pesos.h5')
        break

# Cargar los pesos guardados del modelo

modelo.load_weights('pesos.h5')

# Hacer una prediccion
ultima_secuencia = numeros[-secuencia_longitud:]
ultima_secuencia = np.reshape(ultima_secuencia, (1, secuencia_longitud, 1))
ultima_secuencia = ultima_secuencia / float(9999)
prediccion = modelo.predict(ultima_secuencia)
print('La próxima predicción es: {}'.format(round(prediccion[0][0])))

# Guardar la predicción en un archivo
guardar_prediccion(prediccion)


