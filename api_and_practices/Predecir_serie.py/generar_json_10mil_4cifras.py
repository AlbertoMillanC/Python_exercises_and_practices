import json
import random

numbers = []

while len(numbers) < 10000:
    # generar un número de 4 cifras aleatorio
    num = str(random.randint(0, 9999)).zfill(4)
    # agregar números que comiencen con 000, 00 o 0 y sumen 4 cifras
    if num.startswith(('000', '00', '0')) and sum(int(digit) for digit in num) == 4:
        numbers.append(num)

# guardar los números en un archivo JSON
with open('numeros.json', 'w') as f:
    json.dump({'numeros': numbers}, f)
