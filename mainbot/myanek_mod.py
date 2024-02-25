import message_handler, mailing
from telebot import types
from base import my_anekbd, add_anekbd, delete_anekbd, change_anekbd, show_my_anekbd

def my_anek(bot, message):
    desired_user_id = message.chat.id
    if my_anekbd(desired_user_id) == False:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Добавить")
        btn2 = types.KeyboardButton("Назад")
        markup.row(btn1, btn2)
        bot.send_message(message.chat.id, "У вас нет ни одного анекдота. Хотите добавить?", reply_markup=markup)
    else:
        anekdoti = my_anekbd(desired_user_id)
        anekdot_list = '\n'.join([f'{idx+1}. {anekdot[0]}' for idx, anekdot in enumerate(anekdoti)])
        bot.reply_to(message, f'Твои анекдотики:\n{anekdot_list}')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn3 = types.KeyboardButton("Добавить")
        btn4 = types.KeyboardButton("Изменить")
        markup.row(btn3, btn4)
        btn5 = types.KeyboardButton("Удалить")
        btn6 = types.KeyboardButton("Назад")
        markup.row(btn5, btn6)
        bot.send_message(message.chat.id, "Выберите действие(Напиши номер чтобы увидеть текст):", reply_markup=markup)
        bot.register_next_step_handler(message, lambda msg: my_anek_check(msg, bot))


def my_anek_check(message, bot):
    if (message.text == "Добавить"):
       add_anek(bot, message)
    elif (message.text == "Удалить"):
        delete_anek(bot, message)
    elif (message.text == "Изменить"):
        change_anek(bot, message)
    elif (message.text == "Назад"):
        message_handler.action(bot, message)
    else:
        try:
            # Попытка преобразовать введенный текст в целое число
            anekdot_number = int(message.text)

            # Удаление анекдота с указанным номером из базы данных
            success = show_my_anekbd(message.chat.id, anekdot_number)

            if success == False:
                bot.send_message(message.chat.id, f"Нет анекдота с номером {anekdot_number}.")
                my_anek(bot, message)
            else:
                selected_anek = show_my_anekbd(message.chat.id, anekdot_number)
                bot.send_message(message.chat.id, f"{selected_anek[1]}: \n {selected_anek[2]}")
                my_anek(bot, message)
        except ValueError:
            bot.send_message(message.chat.id, "Введи сообщение или номер.")
            my_anek(bot, message)
     

def add_anek(bot, message):
    bot.send_message(message.chat.id, "Название анекдота:")
    bot.register_next_step_handler(message,lambda msg: get_title(msg, bot))

def get_title(message, bot):
        if (message.text == "Назад"):
            message_handler.action(bot, message)
        else:
            title = message.text
            bot.send_message(message.chat.id, "Текст анекдота:")
            bot.register_next_step_handler(message, lambda msg: get_joke(msg, title, bot))

def get_joke(message, title, bot):
    joke = message.text
    id = message.chat.id
    add_anekbd(title, joke, id)
    bot.send_message(message.chat.id, "Анекдот успешно добавлен")
    my_anek(bot, message)
    mailing.mail(bot, message)



def delete_anek(bot, message):
    bot.send_message(message.chat.id, "Введи номер анекдота, который хочешь удалить:")
    bot.register_next_step_handler(message, lambda msg: process_delete_input(msg, bot))

    
    

def process_delete_input(message, bot):
    try:
        # Попытка преобразовать введенный текст в целое число
        anekdot_number = int(message.text)

        # Удаление анекдота с указанным номером из базы данных
        success = delete_anekbd(message.chat.id, anekdot_number)

        if success:
            bot.send_message(message.chat.id, f"Анекдот с номером {anekdot_number} успешно удален.")
            my_anek(bot, message)
        else:
            bot.send_message(message.chat.id, f"Нет анекдота с номером {anekdot_number}.")
            delete_anek(bot, message)
    except ValueError:
        bot.send_message(message.chat.id, "Некорректный номер")
        my_anek(bot, message)


def change_anek(bot, message):
    bot.send_message(message.chat.id, "Введи номер анекдота, который хочешь изменить:")
    bot.register_next_step_handler(message, lambda msg: process_change_input(msg, bot))

def process_change_input(message, bot):
    try:
        # Попытка преобразовать введенный текст в целое число
        anekdot_number = int(message.text)
        bot.send_message(message.chat.id, "Введите новое название анекдота:")
        bot.register_next_step_handler(message, lambda msg: change_title(msg, anekdot_number, bot))


    except ValueError:
        bot.send_message(message.chat.id, "Некорректный номер")
        change_anek(bot, message)

def change_title(message, anekdot_number, bot):
        if (message.text == "Назад"):
            message_handler.action(bot, message)
        else:
            new_title = message.text
            bot.send_message(message.chat.id, "Введите новый текст анекдота:")
            bot.register_next_step_handler(message, lambda msg: change_text(msg, new_title, anekdot_number, bot))

def change_text(message, new_title, anekdot_number, bot):
    new_text = message.text
    if change_anekbd(message.chat.id, anekdot_number, new_title, new_text):
            bot.send_message(message.chat.id, f"Анекдот с номером {anekdot_number} успешно изменен.")
            my_anek(bot, message)
    else:
            bot.send_message(message.chat.id, f"Не удалось найти анекдот с номером {anekdot_number}.")
            my_anek(bot, message)
