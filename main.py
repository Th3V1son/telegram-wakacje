import telebot
import schedule
import time
import datetime

TOKEN = "haha"
CHANNEL_ID = "no"
bot = telebot.TeleBot(TOKEN, parse_mode=None)

print('bot is online (If you didnt fuck up smth), I guess')


@bot.message_handler(commands=['start'])
def welcum(msg):
    bot.reply_to(msg, "h")


def sendmsg():
    diff = datetime.date(2022,6,24) - datetime.date.today()
    if int(diff.days) == 0:
        bot.send_message(CHANNEL_ID, "🎉 Mamy oficjalnie akacje, miłego brickowania Ximi 🎉")
    else:
        bot.send_message(CHANNEL_ID, "Do wakacji zostało: " + str(diff.days) + " dni")


schedule.every().day.at("00:30").do(sendmsg)

while 1:
    schedule.run_pending()
    time.sleep(1)

bot.infinity_polling()
