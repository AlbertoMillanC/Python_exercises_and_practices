# bot telegram

from crypt import methods


@ app.route('/', methods = [GET', 'POST'])
def index():
    if request.method == 'POST':
       msg = request.get.json()
       try:
        chat_id, txt = tel_parse_messaje(msg)
        if txt == "hi":
            tel_send_message(chat_id, "hello")
            
        if txt == "/help":
            tel_send_message(chat_id, "help")
            tel_send_message(chat_id, "hello i am amix bot")
            tel_send_message(chat_id, "i can help you")
            tel_send_message(chat_id, "one moment please")
            tel_send_message(chat_id, "one moment please help your bot")
            