import json
import numpy as np
import tensorflow as tf
from datetime import datetime
from tensorflow.keras.models import load_model

modelo = load_model('modelo_entrenado.h5')

def guardar_prediccion(prediccion):
    fecha_hora = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    prediccion_str = str(round(prediccion[0][0]))
    try:
        with open('numerosV7.json', 'r') as f:
            data = json.load(f)
    except:
        data = {"predicciones": []}
    predicciones = data.get('predicciones', [])
    predicciones.append({'fecha_hora': fecha_hora, 'prediccion v7': prediccion_str})
    with open('numerosV7.json', 'w') as f:
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
modelo = tf.keras.models.Sequential([
    tf.keras.layers.LSTM(32, input_shape=(X.shape[1], X.shape[2])),
    tf.keras.layers.Dense(1, activation='linear')
])

# Compilar el modelo
modelo.compile(loss='mean_squared_error', optimizer='adam', metrics=['mse'])

# Entrenar el modelo
modelo.fit(X, y, epochs=50, batch_size=32, verbose=3)

# Hacer una predicción
entrada = np.array([numeros[-secuencia_longitud:]])
entrada = entrada / float(9999)
prediccion = modelo.predict(entrada, verbose=0)
prediccion = prediccion * 9999

# Repetir la predicción hasta que sea igual a 9200
for i in range(100):
    entrada = np.array([numeros[-secuencia_longitud:]])
    entrada = entrada / float(9999)
    prediccion = modelo.predict(entrada, verbose=2)
    prediccion = prediccion * 9999
    if round(prediccion[0][0]) == 9200:
        break


# Guardar los parámetros del modelo en un archivo
modelo.save('modelo_entrenado.h5')

print('Predicción: %d' % prediccion)

guardar_prediccion(prediccion)
