# main.py
import os
import telegram
import requests

def bot(request):
    bot = telegram.Bot(token=os.environ["TELEGRAM_TOKEN"])
    if request.method == "POST":
        update = telegram.Update.de_json(request.get_json(force=True), bot)
        if update:
            chat_id = update.message.chat.id
            # Reply with the same message
            url = update.message.text
            bot.sendMessage(chat_id=chat_id, text='got your request...')
#             r = requests.get('https://us-central1-teletrade-323510.cloudfunctions.net/floathook?url=' + url);
#             if r.status_code==200:
#                 reply = r.json()['float']
#             else:
#                 reply = 'sorry, error'
#                 # TODO: add error details
# 
#            bot.sendMessage(chat_id=chat_id, text=reply)

    return "ok, I am alive"
