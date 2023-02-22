import json
import os

json_path = 'api_and_practices/Predecir_serie.py/predecir_redes_neuronales/numeros_ganadores.json'

# Inicializar la variable data con un diccionario vacío
data = {}

if os.path.isfile(json_path):
    with open(json_path) as f:
        data = json.load(f)
    print("El archivo JSON ha sido encontrado con éxito.")
else:
    print(f"No se ha encontrado el archivo JSON en la ruta: {json_path}")

numeros = data.get("numeros", [])  # Utilizar el método get() para acceder a los números y asignar una lista vacía en caso de que no existan

if numeros:
    print("Archivo cargado correctamente")
    print(data)

    # Inicializar los diccionarios para cada columna
    num1 = []
    num2 = []
    num3 = []
    num4 = []

    # Recorrer los números y agregar cada cifra a su respectiva columna
    for numero in numeros:
        cifras = [int(cifra) for cifra in numero]
        num1.append(cifras[0])
        num2.append(cifras[1])
        num3.append(cifras[2])
        num4.append(cifras[3])

    # Crear un nuevo diccionario con las columnas deseadas
    nuevo_data = {
        "Num1": num1,
        "Num2": num2,
        "Num3": num3,
        "Num4": num4,
    }

    # Escribir el nuevo archivo JSON
    with open("numeros_nuevos.json", "w") as f:
        json.dump(nuevo_data, f)
else:
    print("No se han encontrado números en el archivo JSON")
