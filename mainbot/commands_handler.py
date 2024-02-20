from telebot import types

def start(bot, message):
    file_path = 'mainbot/read.txt'
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Да")
    btn2 = types.KeyboardButton("Нет")
    markup.add(btn1, btn2)
    bot.send_message(message.chat.id, content)
    bot.send_message(message.chat.id, f'Привет, {message.from_user.first_name}, хочешь анекдот', reply_markup=markup)

def stop(bot, message):
    bot.reply_to(message, "Бот будет остановлен.")
    bot.stop_polling()

def help(bot, message):
    bot.reply_to(message, f"Вряд-ли я смогу тебе чем-то помочь, {message.from_user.first_name}... Могу только анекдот рассказать на эту тему...")

