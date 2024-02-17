import telebot
import sqlite3
import commands_handler, message_handler
import base
from base import create_table, my_anekbd


bot = telebot.TeleBot('6977419128:AAGv0ygxxpFI5pp_Vy7mGMEvJ8ajKqgPewY')



create_table()

@bot.message_handler(commands=['start', 'stop', 'help'])
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



@bot.message_handler()
def answer1(message):
    if (message.text == 'Да'):
        message_handler.action(bot, message)
    elif (message.text == 'Нет'):
        bot.send_message(message.chat.id, "Зачем написал тогда?")
    elif (message.text == "Случайный анекдот"):
        random(message)
    elif (message.text == "Топ анекдотов"):
        top(message)
    elif (message.text == "Мои анекдоты"):
        my_anek(message)


def my_anek(message):
    bot.send_message(message.chat.id, "Список твоих анекдотов")
    desired_user_id = message.chat.id
    if my_anekbd(desired_user_id) == True:
        bot.send_message(message.chat.id,  "Есть анекдоты")
    else:
        bot.send_message(message.chat.id,  "Нет анекдоты")
    
    
def random(message):
    bot.send_message(message.chat.id, "Купил мужик шляпу а она ему как раз")

def top(message):
    bot.send_message(message.chat.id, "Топ анекдотов по оценкам пользователей")

bot.polling()