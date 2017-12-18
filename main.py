"Бот против панических атак"

import telebot

bot = telebot.TeleBot("472877953:AAF2bachKH0057oBs3fCMlaHJ3J_BRP7Zdo")

print(bot.get_me())

def log(message, answer):
    print("\n -----")
    from datetime import datetime
    print(datetime.now())
    print("Сообщение от {0} {1}. (id = {2}) \n Текст - {3}".format(message.from_user.first_name,
                                                                   message.from_user.last_name,
                                                                   str(message.from_user.id),
                                                                   message.text))
    print(answer)

@bot.message_handler(commands=['start'])
def handle_start(message):
    bot.send_message(message.from_user.id, """Рекомендуем прочитать статью о панических атаках,это может помочь:
http://telegra.ph/Panicheskie-ataki-chto-delat-12-18""")
    user_markup = telebot.types.ReplyKeyboardMarkup(False, False)
    user_markup.row('Я чувствую себя страннно..')
    bot.send_message(message.from_user.id,
                     'Если вы чувствуете панику или страх, воспользуйтесь ботом, это должно помочь',
                     reply_markup=user_markup)

@bot.message_handler(content_types=['text'])
def handle_text(message):
    if message.text == "Я чувствую себя страннно..":
        answer = "Все в порядке!"
        log(message, answer)
        bot.send_message(message.chat.id, answer)
    elif message.text == "/smtiswrong":
        answer = "Все хорошо!"
        log(message, answer)
        bot.send_message(message.chat.id, answer)
    else:
        answer = "Главное помнить, что все хорошо! :3"
        log(message, answer)
        bot.send_message(message.chat.id, answer)


bot.polling(none_stop=True,)
