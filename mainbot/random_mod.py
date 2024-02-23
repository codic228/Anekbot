import message_handler
from telebot import types
from base import random_anek, random_anek_mark_plus, random_anek_mark_minus, complaints_plus

def random(bot, message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Лайк")
    btn2 = types.KeyboardButton("Дизлайк")
    markup.row(btn1, btn2)
    btn3 = types.KeyboardButton("Ошибка в анекдоте")
    btn4 = types.KeyboardButton("Назад")
    markup.row(btn3, btn4)
    ran_an = random_anek()
    bot.send_message(message.chat.id, ran_an[1], reply_markup=markup)
    bot.register_next_step_handler(message,  lambda msg: chek_next_step(msg, ran_an[0], bot))



def chek_next_step(message, id, bot):
    if (message.text == "Лайк"):
        random_anek_mark_plus(id)
        random(bot, message)
    elif (message.text == "Дизлайк"):
        random_anek_mark_minus(id)
        random(bot, message)
    elif (message.text == "Назад"):
        message_handler.action(bot, message)
    elif (message.text == "Ошибка в анекдоте"):
         complaints_plus(id)
         bot.send_message(message.chat.id, "Спасибо!")
         random(bot, message)