import sys
import time
import telebot
from get_text import *
from results import Accuracy

from ../code/main import main
bot = telebot.TeleBot(${{secrets.BOT_TOKEN}})

@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text.lower() == "/start":
        main()
    else:
        return message.text

bot.polling(none_stop=True, interval=0)


def PrintWithSleep(string, sleep_time):
    bot.send_message(message.from_user.id,string)
    time.sleep(sleep_time)


def main():
    # choosing language
    bot.send_message(message.from_user.id, "Select the text language:\n1: English\n2: Русский\n")
    lang = ""
    while (lang := input()) not in {"1", "2"}:
        bot.send_message(message.from_user.id, "Please select 1 or 2")


    # choosing difficulty
    bot.send_message(message.from_user.id, "Select the size of the text:\n1: 20-50 words\n2: 50-100 words\n3: 100-200 words")
    difficulty = ""
    while (difficulty := input()) not in {"1", "2", "3"}:
        bot.send_message(message.from_user.id, "Please select 1 or 2 or 3")


    source = GetSource(lang)
    orig_text = GetText(source, difficulty)
    book = NameOfTheBook(source)


    # competition starts there!
    PrintWithSleep("Are you ready?", 1)
    PrintWithSleep(orig_text, 1.5)
    PrintWithSleep("3", 0.5)
    PrintWithSleep("2", 0.5)
    PrintWithSleep("1", 0.5)
    bot.send_message(message.from_user.id, "Start")

    start_time = time.time()
    your_text = ''
    while (c := sys.stdin.read(1)) != '\n':
        your_text += c
    end_time = time.time()


    # output the result
    duration = end_time - start_time
    accuracy_result = Accuracy(orig_text.strip(), your_text.strip())
    bot.send_message(message.from_user.id, "You made " + accuracy_result + " typos")
    bot.send_message(message.from_user.id, "Your accuracy is: " + str(100 - round(100 * accuracy_result / len(orig_text), 2)) + "%")
    bot.send_message(message.from_user.id, "Time spent: " + str(round(duration, 2)) + " sec")
    bot.send_message(message.from_user.id, "Your speed: " + str(round(len(orig_text) / duration, 2)) + " symbols/sec")
    bot.send_message(message.from_user.id, "This text was from: " + book)

# where main ends
###########################################################################

