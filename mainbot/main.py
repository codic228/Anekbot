import telebot
import commands_handler, message_handler, random_mod, top_mod, myanek_mod
from base import create_table
from telebot import types
bot = telebot.TeleBot('6977419128:AAGv0ygxxpFI5pp_Vy7mGMEvJ8ajKqgPewY')



create_table()

@bot.message_handler(commands=['start', 'stop', 'help', 'menu'])
def handle_start_stop(message):
    if message.text.lower() == '/start':
        commands_handler.start(bot, message)
    elif message.text.lower() == '/stop':
        bot.send_message(message.chat.id, f"Попытка остановить бота от {message.chat.id}...")
        if message.chat.id == 535601294 or message.chat.id == 412106669:
            commands_handler.stop(bot, message)
        else:
            bot.send_message(message.chat.id, "Отказано в доступе.")
    elif message.text.lower() == '/help':
        commands_handler.help(bot, message)
    elif message.text.lower() == '/menu':
        message_handler.action(bot, message)



@bot.message_handler()
def answer1(message):
    if (message.text == 'Да'):
        message_handler.action(bot, message)
    elif (message.text == 'Нет'):
        bot.send_message(message.chat.id, "Зачем написал тогда?")
    elif (message.text == "Случайный анекдот"):
        random_mod.random(bot, message)
    elif (message.text == "Топ анекдотов"):
        top_mod.top(bot, message)
    elif (message.text == "Мои анекдоты"):
        myanek_mod.my_anek(bot, message)
    elif (message.text == "Добавить"):
       myanek_mod.add_anek(bot, message)
    elif (message.text == "Назад"):
        message_handler.action(bot, message)
    elif (message.text == "Удалить"):
        myanek_mod.delete_anek(bot, message)
    elif (message.text == "Изменить"):
        myanek_mod.change_anek(bot, message)
    

bot.infinity_polling()