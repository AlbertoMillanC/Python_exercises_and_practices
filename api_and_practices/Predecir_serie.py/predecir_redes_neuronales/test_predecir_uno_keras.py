import json
import numpy as np
from keras.models import Sequential
from keras.layers import LSTM, Dense

# Cargar datos del archivo JSON
with open('numeros_ganadores.json') as f:
    data = json.load(f)
    
# Preprocesar los datos
numeros = [int(x) for x in data['numeros_ganadores']]
secuencia_longitud = 10  # la longitud de la secuencia de entrada
X = []
y = []
for i in range(len(numeros) - secuencia_longitud):
    secuencia = numeros[i:i+secuencia_longitud]
    objetivo = numeros[i+secuencia_longitud]
    X.append(secuencia)
    y.append(objetivo)
    
# Convertir los datos a matrices numpy
X = np.reshape(X, (len(X), secuencia_longitud, 1))
X = X / float(len(set(numeros)))
y = np.array(y)
y = y / float(len(set(numeros)))

# Crear el modelo de RNN
modelo = Sequential()
modelo.add(LSTM(32, input_shape=(X.shape[1], X.shape[2])))
modelo.add(Dense(1, activation='linear'))

# Compilar el modelo
modelo.compile(loss='mean_squared_error', optimizer='adam', metrics=['accuracy'])

# Entrenar el modelo
modelo.fit(X, y, epochs=100, batch_size=1, verbose=2)

# Evaluar el modelo
puntuacion = modelo.evaluate(X, y, verbose=0)
print('Precisión del modelo: %.2f%%' % (puntuacion[1]*100))

# Hacer una predicción
entrada = np.array([numeros[-secuencia_longitud:]])
entrada = entrada / float(len(set(numeros)))
prediccion = modelo.predict(entrada, verbose=0)
prediccion = prediccion * float(len(set(numeros)))
print('Predicción: %d' % prediccion)
