import message_handler
from telebot import types
from random_modBD import random_anek_mark_plus, random_anek_mark_minus, complaints_plus, act_not_random_anek

def random1(bot, message):
    user_id = message.chat.id
    ran_an = act_not_random_anek(user_id)
    if ran_an == False:
        bot.send_message(message.chat.id,"Похоже ты посмотрел все анекдоты... Очень сильно...\nЧтож, жди новых, можешь пока своих добавить<3")
        message_handler.action(bot, message)
    elif ran_an == True:
        bot.send_message(message.chat.id,"Обалдеть, походу база данных наебнулась или просто в ней нет ни одного анекдота...\nНадеюсь папочка скоро разбереться с этой проблемой и я смогу снова радовать вас анекдотами!")
        message_handler.action(bot, message)
    else:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn0 = types.KeyboardButton("Ещё")
        markup.row(btn0)
        btn1 = types.KeyboardButton("👍")
        btn2 = types.KeyboardButton("👎")
        markup.row(btn1, btn2)
        btn3 = types.KeyboardButton("Ошибка в анекдоте")
        btn4 = types.KeyboardButton("Назад")
        markup.row(btn3, btn4)
        bot.send_message(message.chat.id, f"{ran_an[1]}:\n{ran_an[2]}", reply_markup=markup)
        bot.register_next_step_handler(message,  lambda msg: chek_next_step(msg, ran_an[0], bot))




def chek_next_step(message, id, bot):
    if (message.text == "👍"):
        random_anek_mark_plus(id)
        random1(bot, message)
    elif (message.text == "👎"):
        random_anek_mark_minus(id)
        random1(bot, message)
    elif (message.text == "Назад"):
        message_handler.action(bot, message)
    elif (message.text == "Ошибка в анекдоте"):
         complaints_plus(id)
         bot.send_message(message.chat.id, "Спасибо!")
         random1(bot, message)
    elif (message.text == "Ещё"):
        random1(bot, message)

