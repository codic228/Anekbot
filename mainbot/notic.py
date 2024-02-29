import telebot
from base import add_new_member
bot = telebot.TeleBot('6977419128:AAGv0ygxxpFI5pp_Vy7mGMEvJ8ajKqgPewY')

@bot.message_handler()
def notif(message):
    add_new_member(message.chat.id)
    bot.send_message(message.chat.id, "На сервере ведуться технические работы. скоро бот заработает в прежнем режиме.")

bot.infinity_polling()