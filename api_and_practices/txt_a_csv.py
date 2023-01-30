import csv

# Nombre del archivo de texto
text_file = 'file.txt'

# Nombre del archivo CSV
csv_file = 'file.csv'

# Abrir el archivo de texto
with open(text_file, 'r') as in_file:
    # Leer el contenido del archivo de texto
    lines = in_file.readlines()
    
    # Abrir el archivo CSV
    with open(csv_file, 'w', newline='') as out_file:
        # Crear un objeto de escritura CSV
        writer = csv.writer(out_file)
        
        # Escribir cada línea del archivo de texto en una fila en el archivo CSV
        for line in lines:
            writer.writerow([line.strip()])
