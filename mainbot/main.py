import telebot
import sqlite3
import commands_handler, message_handler
import base
from base import create_table, my_anekbd, add_anekbd
from telebot import types

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
    elif (message.text == "Добавить"):
        add_anek(message)
    elif (message.text == "Назад"):
        message_handler.action(bot, message)


def my_anek(message):
    desired_user_id = message.chat.id
    if my_anekbd(desired_user_id) == False:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Добавить")
        btn2 = types.KeyboardButton("Назад")
        markup.row(btn1, btn2)
        bot.send_message(message.chat.id, "У вас нет ни одного анекдота. Хотите добавить?", reply_markup=markup)
    else:
        anekdoti = my_anekbd(desired_user_id)
        anekdot_list = '\n'.join([f'Название: {anekdot[0]}, Рейтинг: {anekdot[1]}' for anekdot in anekdoti])
        bot.reply_to(message, f'Твои анекдотики:\n{anekdot_list}')



def add_anek(message):
    bot.send_message(message.chat.id, "Название анекдота:")
    bot.register_next_step_handler(message, get_title)

def get_title(message):
    title = message.text
    bot.send_message(message.chat.id, "Текст анекдота:")
    bot.register_next_step_handler(message, lambda msg: get_joke(msg, title))

def get_joke(message, title):
    joke = message.text
    id = message.chat.id
    add_anekbd(title, joke, id)
    bot.send_message(message.chat.id, "Анекдот успешно добавлен")

    
    
def random(message):
    bot.send_message(message.chat.id, "Купил мужик шляпу а она ему как раз")

def top(message):
    bot.send_message(message.chat.id, "Топ анекдотов по оценкам пользователей")

bot.polling()