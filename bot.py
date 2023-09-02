import telebot
from main import mark_the_presence
from datetime import datetime

bot = telebot.TeleBot('6422200295:AAEMNrkBT1u2Obd2UmGzOY4Q09nilmE3Eto')

@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text == "Отметь меня":
        an = mark_the_presence()
        if an == 0:
            bot.send_message(message.from_user.id, "Отметил")

        else:
            bot.send_message(message.from_user.id, "Не смог тебя отметить")
    else:
        bot.send_message(message.from_user.id,
                         "Я тебя не понимаю. Напиши /help.")




bot.polling(none_stop=True, interval=0)