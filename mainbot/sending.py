import telebot
import time
import datetime
from random_mod import from_sending
from random_modBD import act_not_random_anek
from sendingBD import anektime, start_stop_sendingbd
bot = telebot.TeleBot('6977419128:AAGv0ygxxpFI5pp_Vy7mGMEvJ8ajKqgPewY')

start_stop_sendingbd()

def send_message(user_id):
    anek = act_not_random_anek(user_id)
    if anek == False:
        bot.send_message(user_id, "Нету новых анекдотов, прости, не могу тебя порадовать(")
    elif anek == True:
        bot.send_message(user_id, "Обалдеть, походу база данных наебнулась или просто в ней нет ни одного анекдота... Как только появиться я скину!")
    else:
        bot.send_message(user_id, "Твой ежедневный анекдот:")
        bot.send_message(user_id, f"{anek[1]}\n{anek[2]}")

    

flag = True

def main():

    global flag
    while flag:
        current_time = datetime.datetime.now().time()
        time_str = current_time.strftime("%H:%M")
        user_time = anektime() 

        for count in range(0, len(user_time)):
            if user_time[count][2] == 2:
                stop_bot()
                break
            if user_time[count][3] == time_str:
                # bot.send_message(535601294, f"Попытка отправить анек {user_time[count][0]}")
                send_message(user_time[count][0])
        if current_time.minute == 0:
            bot.send_message(535601294, "Бот работает!")

        time.sleep(60)  # Подождать 60 секунд перед следующей проверкой

def stop_bot():
    global flag
    flag = False
    bot.send_message(535601294, "\"sending.py\" будет остановлен.")
    bot.stop_polling()

if __name__ == "__main__":
    main()



bot.infinity_polling()