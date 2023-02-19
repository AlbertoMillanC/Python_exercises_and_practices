import random
import json

def generar_numeros():
    """
    Genera un número aleatorio de 4 cifras.
    Si el número empieza con "000", "00" o "0",
    completa las cifras restantes para sumar 4.
    """
    numero = str(random.randint(0, 9999)).zfill(4)
    while numero.startswith(("000", "00", "0")) and len(numero) < 4:
        numero += str(random.randint(0, 9))
    return numero

# Generar 100,000 números aleatorios de 4 cifras
numeros = [generar_numeros() for _ in range(100000)]

# Agregar 10,000 números que empiezan con "000", "00" o "0" y suman 4 cifras
numeros += ["{:03d}".format(i) for i in range(1000, 10000)]

# Guardar los números en un archivo JSON
with open("numeros.json", "w") as f:
    json.dump({"numeros": numeros}, f)
