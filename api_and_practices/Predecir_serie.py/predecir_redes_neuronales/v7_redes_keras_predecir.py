import numpy as np
import json
from keras.models import load_model
from keras.utils import np_utils


# Cargar los datos desde el archivo JSON
with open('api_and_practices/Predecir_serie.py/predecir_redes_neuronales/numeros_ganadores.json') as f:
    data = json.load(f)
    Num1 = data['Num1']
    Num2 = data['Num2']
    Num3 = data['Num3']
    Num4 = data['Num4']

# Crear una lista con las cifras de cada número
numeros = []
for i in range(len(Num1)):
    cifras = [Num1[i], Num2[i], Num3[i], Num4[i]]
    numeros.append(cifras)

# Crear los conjuntos de entrenamiento y prueba
datos_entrenamiento = np.array(numeros[:len(numeros)-1])
datos_prueba = np.array([numeros[len(numeros)-1]])

# Convertir las cifras a valores entre 0 y 1 para el entrenamiento
X_entrenamiento = datos_entrenamiento / 9
y_entrenamiento = np_utils.to_categorical(np.array(numeros[1:]), num_classes=10)

# Agregar una dimensión adicional a X_entrenamiento para representar los pasos de tiempo
X_entrenamiento = np.reshape(X_entrenamiento, (X_entrenamiento.shape[0], X_entrenamiento.shape[1], 1))

# Cargar el modelo guardado
modelo_cargado = load_model('modelo.hdf5')

# Utilizar el modelo para hacer una predicción sobre un número de 4 cifras
dato_a_predecir = np.array([[0.1, 0.2, 0.3, 0.4]]) # ejemplo de dato a predecir
dato_a_predecir = dato_a_predecir / 9 # convertir las cifras a valores entre 0 y 1
dato_a_predecir = np.reshape(dato_a_predecir, (1, 4, 1)) # agregar una dimensión adicional para representar los pasos de tiempo
prediccion = modelo_cargado.predict(dato_a_predecir) # hacer la predicción
resultado = np.argmax(prediccion, axis=1) # obtener el índice del valor máximo de la predicción
print(resultado)
