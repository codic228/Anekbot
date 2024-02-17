import telebot
import sqlite3
import commands_handler, message_handler
import base
from base import create_table, my_anekbd, add_anekbd, delete_anekbd, change_anekbd
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
    elif (message.text == "Удалить"):
        delete_anek(message)
    elif (message.text == "Изменить"):
        change_anek(message)



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
        anekdot_list = '\n'.join([f'{idx+1}. {anekdot[0]}: \n {anekdot[1]}' for idx, anekdot in enumerate(anekdoti)])
        bot.reply_to(message, f'Твои анекдотики:\n{anekdot_list}')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn3 = types.KeyboardButton("Добавить")
        btn4 = types.KeyboardButton("Изменить")
        markup.row(btn3, btn4)
        btn5 = types.KeyboardButton("Удалить")
        btn6 = types.KeyboardButton("Назад")
        markup.row(btn5, btn6)
        bot.send_message(message.chat.id, "Выберите действие:", reply_markup=markup)



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

def delete_anek(message):
    bot.send_message(message.chat.id, "Введите номер анекдота, который вы хотите удалить:")
    bot.register_next_step_handler(message, process_delete_input)
    

def process_delete_input(message):
    try:
        # Попытка преобразовать введенный текст в целое число
        anekdot_number = int(message.text)

        # Удаление анекдота с указанным номером из базы данных
        success = delete_anekbd(message.chat.id, anekdot_number)

        if success:
            bot.send_message(message.chat.id, f"Анекдот с номером {anekdot_number} успешно удален.")
        else:
            bot.send_message(message.chat.id, f"Не удалось найти анекдот с номером {anekdot_number}.")
    except ValueError:
        bot.send_message(message.chat.id, "Пожалуйста, введите корректный номер анекдота.")    

def change_anek(message):
    bot.send_message(message.chat.id, "Введите номер анекдота, который вы хотите изменить")
    bot.register_next_step_handler(message, process_change_input)

def process_change_input(message):
    try:
        # Попытка преобразовать введенный текст в целое число
        anekdot_number = int(message.text)
        
        bot.send_message(message.chat.id, "Введите новое название анекдота:")
        bot.register_next_step_handler(message, lambda msg: change_title(msg, anekdot_number))
    except ValueError:
        bot.send_message(message.chat.id, "Пожалуйста, введите корректный номер анекдота.")

def change_title(message, anekdot_number):
    new_title = message.text
    bot.send_message(message.chat.id, "Введите новый текст анекдота:")
    bot.register_next_step_handler(message, lambda msg: change_text(msg, new_title, anekdot_number))

def change_text(message, new_title, anekdot_number):
    new_text = message.text
    if change_anekbd(message.chat.id, anekdot_number, new_title, new_text):
            bot.send_message(message.chat.id, f"Анекдот с номером {anekdot_number} успешно изменен.")
    else:
            bot.send_message(message.chat.id, f"Не удалось найти анекдот с номером {anekdot_number}.")
    



def random(message):
    bot.send_message(message.chat.id, "Купил мужик шляпу а она ему как раз")

def top(message):
    bot.send_message(message.chat.id, "Топ анекдотов по оценкам пользователей")

bot.polling()