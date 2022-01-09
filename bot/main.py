import telebot
# token here should be replaced with real bot token
bot = telebot.TeleBot(token)



bot.polling(none_stop=True, interval=0)

