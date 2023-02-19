import json
import numpy as np
from sklearn.model_selection import train_test_split, KFold
from keras.models import Sequential
from keras.layers import LSTM, Dense

# Cargar datos del archivo JSON
with open('api_and_practices/Predecir_serie.py/predecir_redes_neuronales/numeros_ganadores.json') as f:
    data = json.load(f)
    
print(data)


# Preprocesar los datos
numeros = [int(x) for x in data['numeros']]
secuencia_longitud = 10  # la longitud de la secuencia de entrada
X = []
y = []
for i in range(len(numeros) - secuencia_longitud):
    secuencia = numeros[i:i+secuencia_longitud]
    objetivo = numeros[i+secuencia_longitud]
    X.append(secuencia)
    y.append(objetivo)
    
entrada = np.array([numeros[-secuencia_longitud:]])
entrada = entrada / float(len(set(numeros)))
    
# Convertir los datos a matrices numpy
X = np.reshape(X, (len(X), secuencia_longitud, 1))
X = X / float(len(set(numeros)))
y = np.array(y)
y = y / float(len(set(numeros)))

# Dividir los datos en conjuntos de entrenamiento y validación
X_train, X_val, y_train, y_val = train_test_split(X, y, test_size=0.2)

# Crear el modelo de RNN
modelo = Sequential()
modelo.add(LSTM(32, input_shape=(X.shape[1], X.shape[2])))
modelo.add(Dense(1, activation='linear'))

# Compilar el modelo
modelo.compile(loss='mean_squared_error', optimizer='adam', metrics=['accuracy'])

# Definir el número de lotes y la cantidad de épocas por lote
batch_size = 32
epochs = 100

# Entrenar el modelo por lotes y validar en el conjunto de validación
kf = KFold(n_splits=X_train.shape[0] // batch_size)
for train_idx, val_idx in kf.split(X_train):
    X_train_batch, y_train_batch = X_train[train_idx], y_train[train_idx]
    X_val_batch, y_val_batch = X_train[val_idx], y_train[val_idx]
    modelo.fit(X_train_batch, y_train_batch, batch_size=batch_size, epochs=epochs, verbose=2)
    puntuacion = modelo.evaluate(X_val_batch, y_val_batch, verbose=0)
    print('Precisión del modelo en validación: %.2f%%' % (puntuacion[1]*100))

# Evaluar el modelo en el conjunto de prueba
puntuacion = modelo.evaluate(X_val, y_val, verbose=0)
print('Precisión del modelo en prueba: %.2f%%' % (puntuacion[1]*100))

# Hacer una predicción
entrada = entrada / float(len(set(numeros)))
prediccion = modelo.predict(entrada, verbose=0)
prediccion = prediccion * float(len(set(numeros)))
print('Predicción: %d' % prediccion)



