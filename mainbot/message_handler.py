from telebot import types

def action(bot, message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Читать анекдоты")
    markup.row(btn1)
    btn2 = types.KeyboardButton("Топ анекдотов")
    btn3 = types.KeyboardButton("Мои анекдоты")
    markup.row(btn2, btn3)
    btn4 = types.KeyboardButton("Рассылка анекдотов")
    btn5 = types.KeyboardButton("Поддержать проект")
    markup.row(btn4, btn5)
    bot.send_message(message.chat.id, "Выбери действие:", reply_markup=markup)