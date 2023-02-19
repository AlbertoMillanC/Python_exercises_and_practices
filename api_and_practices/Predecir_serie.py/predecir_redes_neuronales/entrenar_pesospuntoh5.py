from keras.models import Sequential
from keras.layers import Dense

# Crear modelo
model = Sequential()
model.add(Dense(8, input_dim=4, activation='relu'))
model.add(Dense(1, activation='sigmoid'))

# Compilar modelo
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

# Entrenar modelo
model.fit(X, y, epochs=150, batch_size=10)

# Guardar los pesos en el archivo 'pesos.h5'
model.save_weights('pesos.h5')
