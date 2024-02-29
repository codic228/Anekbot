from telebot import types
from base import start_stop_sendingbd, all_aneksbd, all_usersbd, show_anekbd, moddelete_bd, modchange_bd

def start(bot, message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Да")
    btn2 = types.KeyboardButton("Нет")
    markup.add(btn1, btn2)
    bot.send_message(message.chat.id, f'Привет, {message.from_user.first_name}, хочешь анекдот', reply_markup=markup)

def stop(bot, message):

    bot.reply_to(message, "Бот будет остановлен.")
    start_stop_sendingbd()
    bot.stop_polling()

def help(bot, message):
    bot.reply_to(message, f"Вряд-ли я смогу тебе чем-то помочь, {message.from_user.first_name}... Могу только анекдот рассказать на эту тему...")


def moder(bot, message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Показать все анекдоты")
    btn2 = types.KeyboardButton("Показать список пользователей")
    markup.row(btn1, btn2)
    bot.send_message(message.chat.id, "Выбери действие:", reply_markup=markup)
    bot.register_next_step_handler(message, lambda msg: moder_next1(msg, bot))

def moder_next1(message, bot):
    if (message.text == "Показать все анекдоты"):
        show_anek(message, bot)
    elif (message.text == "Показать список пользователей"):
        show_users(message, bot)

def show_users(message, bot):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Назад")
        markup.row(btn1)
        users = all_usersbd()
        users_list = '\n'.join([f'{idx+1}. {users[0]}|{users[1]}|{users[2]}|({users[3]})|' for idx, users in enumerate(users)])
        bot.reply_to(message, f'Номер в списке. | Номер в БД | ID пользователя | issub | Время |\n{users_list}', reply_markup=markup)
        bot.register_next_step_handler(message, lambda msg: ch_user(msg, bot))

def ch_user(message, bot):
    if (message.text == "Назад"):
        moder(bot, message)
    

def show_anek(message, bot):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Назад")
    markup.row(btn1)
    aneki = all_aneksbd()
    anekdot_list = '\n'.join([f'{idx+1}. {aneki[0]}|{aneki[1]}|{aneki[2]}|({aneki[3]})|({aneki[4]})|' for idx, aneki in enumerate(aneki)])
    bot.reply_to(message, f'Номер в списке. | Номер в БД | Название | Рейтинг | ID Создателя | Ошибки |\n{anekdot_list}')
    bot.send_message(message.chat.id, "Напиши номер чтобы посмотреть анекдот:", reply_markup=markup)
    bot.register_next_step_handler(message, lambda msg: open_anek(msg, bot))


def open_anek(message, bot):
    if (message.text == "Назад"):
        moder(bot, message)
    else:
        try:
            # Попытка преобразовать введенный текст в целое число
            anekdot_number = int(message.text)

            # Удаление анекдота с указанным номером из базы данных
            success = show_anekbd(anekdot_number)

            if success == False:
                bot.send_message(message.chat.id, f"Нет анекдота с номером {anekdot_number}.")
                show_anek(message, bot)
            else:
                markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
                btn1 = types.KeyboardButton("Удалить")
                btn2 = types.KeyboardButton("Изменить")
                markup.row(btn1, btn2)
                btn3 = types.KeyboardButton("Назад")
                markup.row(btn3)
                bot.send_message(message.chat.id, "Выбери действие:", reply_markup=markup)
                selected_anek = show_anekbd(anekdot_number)
                bot.send_message(message.chat.id, f"{selected_anek[1]}: \n {selected_anek[2]}")
                bot.register_next_step_handler(message, lambda msg:moder_next2(msg, anekdot_number, bot))
        except ValueError:
            bot.send_message(message.chat.id, "Введи сообщение или номер.")
            show_anek(message, bot)

def moder_next2(message, anekdot_number, bot):
    if (message.text == "Удалить"):
        moddelete_bd(anekdot_number)
        bot.send_message(message.chat.id, f"Анекдот с номером {anekdot_number} успешно удален.")
        show_anek(message, bot)
    elif (message.text == "Изменить"):
        change_anek(bot, message, anekdot_number)
    elif (message.text == "Назад"):
        show_anek(message, bot)


def change_anek(bot, message, anekdot_number):
    bot.send_message(message.chat.id, "Введите новое название анекдота:")
    bot.register_next_step_handler(message, lambda msg: change_title(msg, anekdot_number, bot))


def change_title(message, anekdot_number, bot):
        if (message.text == "Назад"):
            show_anek(message, bot)
        else:
            new_title = message.text
            bot.send_message(message.chat.id, "Введите новый текст анекдота:")
            bot.register_next_step_handler(message, lambda msg: change_text(msg, new_title, anekdot_number, bot))

def change_text(message, new_title, anekdot_number, bot):
    new_text = message.text
    modchange_bd(anekdot_number, new_title, new_text)
    bot.send_message(message.chat.id, f"Анекдот с номером {anekdot_number} успешно изменен.")
    show_anek(message, bot)

    