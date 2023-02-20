from keras.models import Sequential
from keras.layers import Dense
from keras.models import load_model

# Crear modelo
modelo = Sequential()
modelo.add(Dense(64, activation='relu', input_dim=80))
modelo.add(Dense(64, activation='relu'))
modelo.add(Dense(10, activation='softmax'))

# Compilar modelo
modelo.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

# Entrenar modelo
modelo.fit(X_entrenamiento, y_entrenamiento, epochs=10, batch_size=32)

# Guardar modelo
modelo.save('modelo.hdf5')

# Cargar modelo desde archivo
modelo_cargado = load_model('modelo.hdf5')
from keras.models import Sequential
from keras.layers import Dense

# Generar datos de entrenamiento
X_train = []
y_train = []
for i in range(1000, 10000):
    X_train.append([int(digit) for digit in str(i)])
    y_train.append(i % 2)

# Dividir los datos en entrenamiento y validación
X_val = X_train[8000:]
y_val = y_train[8000:]
X_train = X_train[:8000]
y_train = y_train[:8000]

# Crear modelo
model = Sequential()
model.add(Dense(64, activation='relu', input_shape=(4,)))
model.add(Dense(64, activation='relu'))
model.add(Dense(1, activation='sigmoid'))

# Compilar modelo
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

# Entrenar modelo
model.fit(X_train, y_train, epochs=10, batch_size=32, validation_data=(X_val, y_val))

# Evaluar modelo en datos de prueba
X_test = [[1, 2, 3, 4], [2, 3, 4, 5], [3, 4, 5, 6], [4, 5, 6, 7], [5, 6, 7, 8], [6, 7, 8, 9], [7, 8, 9, 0], [8, 9, 0, 1]]
y_test = [0, 1, 0, 1, 0, 1, 1, 0]
loss, accuracy = model.evaluate(X_test, y_test)

# Guardar modelo
model.save('modelo.hdf5')
