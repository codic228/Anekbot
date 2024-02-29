import telebot
import commands_handler, message_handler, random_mod, top_mod, myanek_mod, mailing
from base import create_table, create_table1, add_new_member
from telebot import types
import random
bot = telebot.TeleBot('6977419128:AAGv0ygxxpFI5pp_Vy7mGMEvJ8ajKqgPewY')


create_table()
create_table1()
@bot.message_handler(commands=['start', 'stop', 'help', 'menu', 'send', 'moder'])
def handle_start_stop(message):
    if message.text.lower() == '/start':
        add_new_member(message.chat.id)
        commands_handler.start(bot, message)
    elif message.text.lower() == '/stop':
        bot.send_message(message.chat.id, f"Попытка остановить бота от {message.chat.id}...")
        if message.chat.id == 535601294 or message.chat.id == 412106669:
            commands_handler.stop(bot, message)
        else:
            bot.send_message(message.chat.id, "Отказано в доступе.")
    elif message.text.lower() == '/help':
        commands_handler.help(bot, message)
    elif message.text.lower() == '/moder':
        bot.send_message(message.chat.id, f"Введите пароль:")
        bot.register_next_step_handler(message, moder_check)
    elif message.text.lower() == '/menu':
        message_handler.action(bot, message)
    # elif message.text.lower() == '/send':
    #     if (message.chat.id == 535601294):
    #         bot.send_message(message.chat.id, "Введи сообщение.")
    #         bot.register_next_step_handler(message, lambda msg: send(msg, bot))
    #     else:
    #         bot.send_message(message.chat.id, "Отказано в доступе.")

# def send(message, bot):
#     bot.send_message(6849041155, f"{message.text}")
        
def moder_check(message):
    pasw = "anekbot2855"
    if (message.text == pasw or message.chat.id == 535601294):
        bot.send_message(message.chat.id, f"Добро пожаловать в меню для модераторов.")
        commands_handler.moder(bot, message)
    else: 
        bot.send_message(message.chat.id, f"Доступ запрещен.")

@bot.message_handler()
def answer1(message):
    if (message.text == 'Да'):
        message_handler.action(bot, message)
    elif (message.text == 'Нет'):
        bot.send_message(message.chat.id, "Зачем написал тогда?")
    elif (message.text == "Читать анекдоты"):
        random_mod.random1(bot, message)
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
    elif (message.text == "Рассылка анекдотов"):
        mailing.mail(bot, message)
    elif (message.text == "Отменить"):
        message_handler.action(bot, message)
    elif (message.text == "Поддержать проект"):
        bot.send_message(message.chat.id, "Хз я по приколу добавил эту кнопку ну если у вас есть желание скинуть мне денег то можете воспользоваться этим кодом, спасибо")
        image_path = r'E:\\User1\\Рабочие области vscode\\Anekbot\\mainbot\\qrcode.jpg'
        with open(image_path, 'rb') as photo:
            bot.send_photo(message.chat.id, photo)
    else:
        random_number = random.randint(1, 5)
        if (random_number == 1):
            bot.send_message(message.chat.id, "Чувак я не нейросеть я не понимаю че ты говоришь")
        elif (random_number == 2):
            bot.send_message(message.chat.id, "Я только анекдоты рассказываю")
        elif (random_number == 3):
            bot.send_message(message.chat.id, "Да бля напиши по делу что-то")
        elif (random_number == 4):
            bot.send_message(message.chat.id, "Эти сообщения вообще просто записаны в коде и рандомно отправляются когда ты чето не то пишешь гений")
        elif (random_number == 4):
            bot.send_message(message.chat.id, "Умоляю просто ответь нормально на мой предыдущий запрос")
        elif (random_number == 5):
            bot.send_message(message.chat.id, "Письки")


bot.infinity_polling()