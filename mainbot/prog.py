import telebot
import commands_handler, message_handler, add_new
from telebot import types
from base import create_table, add_anekdot, get_anekdots, rand_anekdot


bot = telebot.TeleBot('6977419128:AAGv0ygxxpFI5pp_Vy7mGMEvJ8ajKqgPewY')

# Создаем таблицу в БД
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
    elif (message.text == "Категории"):
        category(message)
    elif (message.text == "Топ анекдотов"):
        top(message)
    elif (message.text == "Добавить анекдот"):
        add_new.add_py(bot, message)


def category(message):
    bot.send_message(message.chat.id, "Выбери категорию:")

def random(message):
    random_joke = rand_anekdot()
    bot.send_message(message.chat.id, random_joke)

def top(message):
    # Получаем список анекдотов и отправляем их в чат
    anekdots = get_anekdots()
    anekdot_list = '\n'.join([f'{anekdot[0]}. {anekdot[1]} (Категория: {anekdot[3]}, Рейтинг: {anekdot[4]})' for anekdot in anekdots])
    bot.reply_to(message, f'Топ анекдотов:\n{anekdot_list}')

bot.polling()