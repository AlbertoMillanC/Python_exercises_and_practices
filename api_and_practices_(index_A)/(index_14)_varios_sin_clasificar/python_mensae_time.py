import webbrowser

# Obtén el número de teléfono y el mensaje a enviar desde el usuario
phone_number = input("Ingrese el número de teléfono de WhatsApp (incluyendo el código de país): ")
message = input("Ingrese el mensaje a enviar: ")

# Crea la URL para enviar el mensaje de WhatsApp
url = f'https://api.whatsapp.com/send?phone={phone_number}&text={message}'

# Abre la URL en el navegador predeterminado del sistema
webbrowser.open(url)
