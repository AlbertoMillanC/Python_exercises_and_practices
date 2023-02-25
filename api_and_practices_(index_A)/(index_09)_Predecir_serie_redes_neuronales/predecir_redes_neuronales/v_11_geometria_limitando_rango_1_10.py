import json
import datetime
import numpy as np
import pandas as pd
from tensorflow import keras
from sklearn.model_selection import train_test_split
from tensorflow.keras.models import load_model
from sklearn.metrics import mean_squared_error

# definir función de activación personalizada que limite las salidas al rango de 1 a 10
def custom_activation(x):
    return 5 * (keras.activations.tanh(x) + 0)

# cargar los datos desde el archivo CSV
data = pd.read_csv('datos_red_grupos8.csv')

# dividir los datos en conjuntos de entrenamiento y prueba
X = data.iloc[:, :-4]
y = data.iloc[:, -4:]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# cargar el modelo previamente entrenado
modelo = load_model('modelo_figurasv11.h5', custom_objects={'custom_activation': custom_activation})

# definir el modelo de la red neuronal
model = keras.Sequential([
    keras.layers.Dense(512, activation='relu', input_shape=[4]),
    keras.layers.Dense(256, activation='relu'),
    keras.layers.Dense(4, activation=custom_activation)
])

# compilar el modelo
model.compile(optimizer='adam', loss='mean_squared_error', metrics=['mae'])

# entrenar el modelo
model.fit(X_train, y_train, epochs=1000)

# evaluar el modelo
test_loss, test_mae = model.evaluate(X_test, y_test)
print(f"Mean Absolute Error: {test_mae}")
mse = mean_squared_error(y_train, y_train)
print(f"MSE:{mse}")

# guardar el modelo en un archivo
timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
model.save(f'modelo_figurasv11.h5')

# hacer predicciones
nuevas_figuras = np.array([[9, 10, 6, 8], [1, 10, 3, 9], [9, 7, 7, 10]])
predicciones = model.predict(nuevas_figuras)

# escalar los valores de salida al rango de 1 a 10
predicciones = (predicciones )

# guardar las predicciones en un archivo JSON con la hora en que se guarda
resultado = {
    'timestamp': datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S"),
    'predicciones': predicciones.tolist()
}
with open(f'predicciones_figurasv11.json', 'w') as f:
    json.dump(resultado, f)

print(resultado)
