from base import add_anekdot


def add_py(bot, message):
    bot.send_message(message.chat.id, "Напиши заголовок анекдота:")
    bot.register_next_step_handler(message, get_title, bot)

def get_title(message, bot):
    title = message.text
    bot.send_message(message.chat.id, "Теперь напиши сам анекдот:")
    bot.register_next_step_handler(message, lambda msg: get_joke(msg, title, bot))

def get_joke(message, title, bot):
    joke = message.text
    bot.send_message(message.chat.id, "Укажи категорию анекдота:")
    bot.register_next_step_handler(message, lambda msg: get_category(msg, title, joke, bot))

def get_category(message, title, joke, bot):
    category = message.text
    bot.send_message(message.chat.id, "Укажи рейтинг анекдота (целое число):")
    bot.register_next_step_handler(message, lambda msg: get_rating(msg, title, joke, category, bot))

def get_rating(message, title, joke, category, bot):
    try:
        rating = int(message.text)
        add_anekdot(title, joke, category, rating)
        bot.send_message(message.chat.id, "Анекдот успешно добавлен!")
    except ValueError:
        bot.send_message(message.chat.id, "Рейтинг должен быть целым числом. Попробуй еще раз.")