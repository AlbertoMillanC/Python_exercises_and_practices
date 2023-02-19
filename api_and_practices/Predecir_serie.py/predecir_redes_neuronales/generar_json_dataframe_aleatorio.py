import random
import json

# Crear una lista vacía para almacenar los datos generados aleatoriamente
data = []

# Generar 100 ejemplos de datos
for i in range(100):
    # Generar los datos aleatorios
    num1 = random.randint(1, 69)
    num2 = random.randint(1, 69)
    num3 = random.randint(1, 69)
    num4 = random.randint(1, 69)
    num5 = random.randint(1, 69)
    powerball = random.randint(1, 26)
    jackpot = random.randint(1000000, 1000000000)

    # Agregar los datos a la lista
    data.append({
        'X': {
            'Num1': num1,
            'Num2': num2,
            'Num3': num3,
            'Num4': num4,
            'Num5': num5,
            'Powerball': powerball
        },
        'y': jackpot
    })

# Escribir los datos en un archivo JSON
with open('numeros_ganadores.json', 'w') as file:
    json.dump(data, file)
