from telebot import types

def action(bot, message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Случайный анекдот")
    btn2 = types.KeyboardButton("Категори")
    markup.row(btn1, btn2)
    btn3 = types.KeyboardButton("Топ анекдотов")
    btn4 = types.KeyboardButton("Добавить анекдот")
    markup.row(btn3, btn4)
    bot.send_message(message.chat.id, "Выбери действие:", reply_markup=markup)