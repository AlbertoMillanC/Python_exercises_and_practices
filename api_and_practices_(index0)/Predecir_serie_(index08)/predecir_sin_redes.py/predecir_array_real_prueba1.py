import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# Crear un array con 40 números para entrenamiento y otro con 20 para prueba
numeros = ['8942', '7121', '6822', '3137', '4797', '8562', '5908', '5694', '0069', '4247', '0400', '5307', '8219', '3579', '5596', '4513', '4457', '8975', '7361', '4004', '9359', '0840', '0575', '7240', '5526', '3177', '8312', '6876', '7252', '7981', '7206', '9739', '8693', '0229', '3747', '2637', '1336', '0278', '9437', '5481', '7776', '7985', '4634', '1473', '6944', '6819', '2008', '7277', '1606', '9855', '4711', '7987', '0303', '6017', '1010', '4770', '1522', '8811', '2242', '2000', '8867', '0409', '0636', '6551', '0234', '1541', '7435', '7263', '0268', '8750', '0796', '6057', '3331', '4617', '4959', '8405', '3894', '8138', '3554', '3174', '0379', '5855', '1999', '2153', '0223', '0517', '9196', '5295', '2605', '3067', '6899', '1528', '3372', '8708', '0457', '8772', '2564', '6737', '1866', '6520']
numeros_entrenamiento = numeros[:60]
numeros_prueba = numeros[20:]

datos = pd.DataFrame({'Numero': numeros_entrenamiento})

# Convertir los números a enteros
datos['Numero'] = datos['Numero'].astype(int)

# Añadir columnas para representar los 6 últimos números ganadores
for i in range(0, 6):
    datos[f'Ganador{i}'] = datos['Numero'].shift(i).astype(int)

# Eliminar las filas que contienen valores nulos
datos = datos.dropna()


# Dividir los datos en conjuntos de entrenamiento y prueba
x_entrenamiento, x_prueba, y_entrenamiento, y_prueba = train_test_split(
    datos.iloc[:, :-1], datos.iloc[:, -1], test_size=0.35, random_state=0)

# Crear y ajustar el modelo de regresión lineal
modelo = LinearRegression()
modelo.fit(x_entrenamiento, y_entrenamiento)

# Hacer una predicción en base a los 6 últimos números ganadores
serie_anterior = numeros_prueba[-6:]
proximo_numero = modelo.predict([serie_anterior])[0]
print(f'El próximo número ganador es: {int(proximo_numero)}')
