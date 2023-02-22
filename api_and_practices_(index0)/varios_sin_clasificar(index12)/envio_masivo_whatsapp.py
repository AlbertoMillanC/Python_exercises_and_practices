import csv
import webbrowser

# Abre el archivo CSV
with open('numbers.csv', 'r') as file:
    reader = csv.reader(file)

    # Salta la primera línea (encabezado)
    next(reader)

    # Recorre las filas del archivo CSV
    for row in reader:
        phone_number = row[0]
        message = row[1]

        # Crea la URL para enviar el mensaje de WhatsApp
        url = f'https://api.whatsapp.com/send?phone={phone_number}&text={message}'

        # Abre la URL en el navegador predeterminado del sistema
        webbrowser.open(url)
