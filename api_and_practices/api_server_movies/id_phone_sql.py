import pyodbc
import json

def buscar_telefono(telefono):
    # Crea la conexión a la base de datos
    conn = pyodbc.connect(
        "Driver={SQL Server};"
        "Server=localhost;"
        "Database=mi_bd;"
        "Trusted_Connection=yes;"
    )

    # Crea el cursor para ejecutar la consulta
    cursor = conn.cursor()

    # Ejecuta la consulta para obtener el registro que contiene el número de teléfono buscado
    cursor.execute("SELECT * FROM contactos WHERE telefono = ?", telefono)

    # Obtiene el resultado de la consulta
    resultado = cursor.fetchone()

    # Convierte el resultado a formato JSON
    resultado_json = json.dumps(resultado)

    # Cierra la conexión a la base de datos
    conn.close()

    # Devuelve el resultado en formato JSON
    return resultado_json

# Llamada a la función con un número de teléfono de ejemplo
resultado = buscar_telefono("1234567890")

print(resultado)
