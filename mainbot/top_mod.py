import message_handler
from telebot import types
from base import top_anek_bd, top_anek_bd_select


def top(bot, message):
    top_anekov = top_anek_bd()
    anekdot_list = '\n'.join([f'{idx+1}. {top_anekov[1]}, Рейтинг: ({top_anekov[3]}):' for idx, top_anekov in enumerate(top_anekov)])
    bot.reply_to(message, f'Топ 10 анекдотов(по оценкам пользователей):\n{anekdot_list}')
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Назад")
    markup.row(btn1)
    bot.send_message(message.chat.id, 'Напиши номер анекдота чтобы посмотреть его:', reply_markup=markup)
    bot.register_next_step_handler(message, lambda msg: top_select(msg, bot))

def top_select(message, bot):
    if (message.text == "Назад"):
        message_handler.action(bot, message)
    else:
        try:
            number = int(message.text)
            if (number > 10):
                bot.send_message(message.chat.id, "Это топ 10 тут всего 10 записей бро")
                top(bot, message)
            else:
                top_anekov = top_anek_bd_select(number -1)
                anekdot_list = '\n'.join([f'{top_anekov[1]}: \n {top_anekov[2]}' for top_anekov in top_anekov])
                bot.send_message(message.chat.id, anekdot_list)
                top(bot, message)
        except ValueError:
            bot.send_message(message.chat.id, "бля попросил же номер написать")
            top(bot, message)

