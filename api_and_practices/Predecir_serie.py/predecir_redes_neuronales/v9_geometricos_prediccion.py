import json
import datetime
import numpy as np
import pandas as pd
from tensorflow import keras
from sklearn.model_selection import train_test_split

# cargar los datos desde el archivo CSV
data = pd.read_csv('datos_figuras.csv')

# dividir los datos en conjuntos de entrenamiento y prueba
X = data.iloc[:, :-4]
y = data.iloc[:, -4:]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# definir el modelo de la red neuronal
model = keras.Sequential([
    keras.layers.Dense(64, activation='relu', input_shape=[4]),
    keras.layers.Dense(64, activation='relu'),
    keras.layers.Dense(4)
])

# compilar el modelo
model.compile(optimizer='adam', loss='mean_squared_error')

# entrenar el modelo
model.fit(X_train, y_train, epochs=50)

# evaluar el modelo
test_loss = model.evaluate(X_test, y_test)

# guardar el modelo en un archivo
timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
model.save(f'modelo_figuras_{timestamp}.h5')

# hacer predicciones
nuevas_figuras = np.array([[4, 11, 6, 8], [1, 2, 3, 4], [7, 7, 7, 7]])
predicciones = model.predict(nuevas_figuras)

# guardar las predicciones en un archivo JSON con la hora en que se guarda
resultado = {
    'timestamp': datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S"),
    'predicciones': predicciones.tolist()
}
with open(f'predicciones_figuras_{timestamp}.json', 'w') as f:
    json.dump(resultado, f)
