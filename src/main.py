import os
import telegram


def bot(request):
    bot = telegram.Bot(token=os.environ["TELEGRAM_TOKEN"])
    if request.method == "POST":
        update = telegram.Update.de_json(request.get_json(force=True), bot)
        if update:
            chat_id = update.message.chat.id

            message = update.message.text
            bot.sendMessage(chat_id=chat_id,
                            text=f'got your request... you sent: {message}')

    return "this should never happen"
