import os
import telegram
import requests


def bot(request):
    bot = telegram.Bot(token=os.environ["TELEGRAM_TOKEN"])
    if request.method == "POST":
        update = telegram.Update.de_json(request.get_json(force=True), bot)
        if update:
            chat_id = update.message.chat.id

            message = update.message.text
            response = requests.get("https://meme-api.herokuapp.com/gimme")
            if response.status_code == 200:
                url = response.json()["url"]
                bot.sendMessage(chat_id=chat_id,
                                text=f"got your request... you sent: {message}\n"
                                + f"here is your meme: {url}")

    return "this should never happen"
