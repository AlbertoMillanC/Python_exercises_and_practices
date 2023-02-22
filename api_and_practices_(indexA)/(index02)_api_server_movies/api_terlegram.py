import telegram

# Inicializamos el bot con el token de autenticación
bot = telegram.Bot(token="MI_TOKEN_DE_AUTENTICACION")

# Obtenemos la información del usuario al que queremos enviar el mensaje
user = bot.get_chat(chat_id="MI_ID_DE_USUARIO")

# Creamos el mensaje de aceptación de condiciones
message = "Hola, gracias por utilizar nuestro servicio. Por favor, acepta nuestras condiciones de uso para continuar."

# Enviamos el mensaje al usuario
bot.send_message(chat_id=user.id, text=message)
