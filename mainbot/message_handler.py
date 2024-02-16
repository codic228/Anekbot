from telebot import types

def action(bot, message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Случайный анекдот")
    markup.row(btn1)
    btn3 = types.KeyboardButton("Топ анекдотов")
    btn4 = types.KeyboardButton("Мои анекдоты")
    markup.row(btn3, btn4)
    bot.send_message(message.chat.id, "Выбери действие:", reply_markup=markup)