import numpy as np
import pandas as pd
import tensorflow as tf
from tensorflow import keras

# Cargar los datos de entrada
datos = pd.read_csv('datos_del_sorteo_comas.csv')
X = datos.drop('ganadora', axis=1).values
y = datos['ganadora'].values

# Normalizar los datos
X = X / 99.0
y = y / 99.0

# Dividir los datos en conjunto de entrenamiento y de prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Crear el modelo de red neuronal
modelo = keras.models.Sequential([
    keras.layers.Dense(32, input_shape=(X.shape[1],)),
    keras.layers.Dense(16, activation='relu'),
    keras.layers.Dense(1, activation='linear')
])

# Compilar el modelo
modelo.compile(loss='mean_squared_error', optimizer='adam', metrics=['mse'])

# Entrenar el modelo
modelo.fit(X_train, y_train, epochs=50, batch_size=32, validation_data=(X_test, y_test))

# Evaluar el modelo en el conjunto de prueba
loss, mse = modelo.evaluate(X_test, y_test)
print(f"Pérdida en el conjunto de prueba: {loss:.2f}, Error cuadrático medio: {mse:.2f}")

# Hacer una predicción
entrada = np.array([[0.1, 0.2, 0.3, 0.4, 0.5]])
prediccion = modelo.predict(entrada)
print(f"La predicción es: {prediccion[0, 0]:.2f}")
