from base import  subscribebd, check_sub, unsubscribedbd
import message_handler
from telebot import types
import re



def mail(bot, message):
    if check_sub(message.chat.id) == True:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Изменить время")
        markup.row(btn1)
        btn3 = types.KeyboardButton("Отменить подписку")
        btn2 = types.KeyboardButton("Назад")
        markup.row(btn3, btn2)
        bot.send_message(message.chat.id, "Выбери действие:", reply_markup=markup)
        bot.register_next_step_handler(message, lambda msg: mail_next(msg, bot))
    else:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Подписаться на рассылку(БЕСПЛАТНО)")
        btn2 = types.KeyboardButton("Назад")
        markup.row(btn1, btn2)
        bot.send_message(message.chat.id, "Выбери действие:", reply_markup=markup)
        bot.register_next_step_handler(message, lambda msg: mail_next(msg, bot))

def mail_next(message, bot):
    if (message.text == "Подписаться на рассылку(БЕСПЛАТНО)"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn2 = types.KeyboardButton("Отменить")
        markup.row(btn2)
        bot.send_message(message.chat.id, "Напишите время в которое вы хотите получать анекдот(в формате HH:MM)", reply_markup=markup)
        bot.register_next_step_handler(message, lambda msg: subscribe(msg, bot))
    elif (message.text == "Изменить время"):
        bot.send_message(message.chat.id, "Напишите время в которое вы хотите получать анекдот(в формате HH:MM)")
        bot.register_next_step_handler(message, lambda msg: subscribe(msg, bot))
    elif (message.text == "Отменить подписку"):
        unsubscribedbd(message.chat.id)
        bot.send_message(message.chat.id, 'Успешно!')
        message_handler.action(bot, message)
    elif (message.text == "Назад"):
        message_handler.action(bot, message)


def subscribe(message, bot):
    if (message.text == "Отменить"):
        message_handler.action(bot, message)
    else:
        if is_valid_time(message.text):
            subscribebd(message.chat.id, message.text)
            bot.send_message(message.chat.id, 'Успешно!')
            message_handler.action(bot, message)
        else:
            bot.send_message(message.chat.id, 'Ввдите время в правильном формате')
            bot.register_next_step_handler(message, lambda msg: subscribe(msg, bot))


def is_valid_time(input_time):
    pattern = re.compile(r'^([01]\d|2[0-3]):([0-5]\d)$')
    return bool(re.match(pattern, input_time))




    