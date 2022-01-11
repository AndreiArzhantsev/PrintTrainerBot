import sys
import time
import telebot
from telebot import custom_filters
from get_text import *
from results import Accuracy


class States:
    lang = 1
    size = 2
    your_text = 3
    orig_text = ''
    book = ''
    start_time = 0
    end_time = 0


token = "5089220566:AAGM006zFa-b2f2RniRRmNrbudcZY8_TwmA"
bot = telebot.TeleBot(token)


@bot.message_handler(commands='start')
def WelcomeMsg(message):
    bot.send_message(message.from_user.id, "Hello there, I'm PrintTrainerBot. Type /train to start training. Also try /help for more info")


@bot.message_handler(commands='help')
def HelpMsg(message):
    bot.send_message(message.from_user.id, '''Hello again friend.
Let me introduce myself. I am quite simple bot. All I can do is help you to practice so called 'touch typing' - I send you a text, and you type it back as fast as you can. Then I send you your result. Practice more and more and soon you'll observe your progress. Good luck. Oh, and there are my commands:
/start launches me and outputs enterred message.
/help provides description of what I can do.
/train starts your training - try it for sure!
/cancel cancels the current operation.
''')

@bot.message_handler(commands='train')
def StartTraining(message):
    bot.set_state(message.from_user.id, States.lang)
    bot.send_message(message.from_user.id, str(chr(0x1F524)) + "Select the text language:\n"+
        "1:English"  + "\n" +
        "2:Русский")


@bot.message_handler(state="*", commands='cancel')
def Cancel(message):
    bot.send_message(message.from_user.id, "Canceled")
    bot.delete_state(message.from_user.id)


@bot.message_handler(commands='cancel')
def Cancel(message):
    bot.send_message(message.from_user.id, "Canceled")


@bot.message_handler(state=States.lang)
def SetLanguage(message):
    if (message.text in {"1", "2"}):
        bot.send_message(message.from_user.id, str(chr(0x1F4DA)) + "Select the size of the text:\n1: 20-50 words\n2: 50-100 words\n3: 100-200 words")
        bot.set_state(message.from_user.id, States.size)
        with bot.retrieve_data(message.from_user.id) as data:
            data['lang'] = message.text
    else:
        bot.send_message(message.from_user.id, "Please select 1 or 2")


@bot.message_handler(state=States.size)
def SetRemaining(message):
    if (message.text in {"1", "2", "3"}):
        bot.set_state(message.from_user.id, States.your_text)
        with bot.retrieve_data(message.from_user.id) as data:
            data['size'] = message.text
            source = GetSource(data['lang'])
            data['orig_text'] = GetText(source, data['size'])
            data['book'] = NameOfTheBook(source)

            bot.send_message(message.from_user.id, str(chr(0x026A1)) + "Are you ready?")
            time.sleep(1)
            bot.send_message(message.from_user.id, data['orig_text'])
            time.sleep(1.5)
            bot.send_message(message.from_user.id, str(chr(0x1F534)))
            time.sleep(0.3)
            bot.send_message(message.from_user.id, str(chr(0x1F7E1)))
            time.sleep(0.3)
            bot.send_message(message.from_user.id, str(chr(0x1F7E2)))
            time.sleep(0.3)
            bot.send_message(message.from_user.id, str(chr(0x1F680)) + "Start")
            data['start_time'] = time.time()
    else:
        bot.send_message(message.from_user.id, "Please select 1 or 2 or 3")


@bot.message_handler(state=States.your_text)
def GetUserText(message):
    with bot.retrieve_data(message.from_user.id) as data:
        data['end_time'] = time.time()
        data['your_text'] = message.text
        duration = data['end_time'] - data['start_time']
        accuracy_result = Accuracy(data['orig_text'].strip(), data['your_text'].strip())
        bot.send_message(message.from_user.id,
            str(chr(0x1F5D1)) + "You made " + str(accuracy_result) + " typos" + "\n" +
            str(chr(0x1F3AF)) + "Your accuracy: " + str(100 - round(100 * accuracy_result / len(data['orig_text']), 2)) + "%" + "\n" + 
            str(chr(0x0231B)) + "Time spent: " + str(round(duration, 2)) + " sec" + "\n" +
            str(chr(0x1F6B4)) + "Your speed: " + str(round(60 * len(data['orig_text']) / duration, 2)) + " symbols/min" + "\n" +
            str(chr(0x1F4D7)) + "This text was from: " + data['book'])
    bot.delete_state(message.from_user.id)


@bot.message_handler(content_types='text')
def ReportUnknownMsg(message):
    if (message.text.lower() == "i love you"):
        bot.send_message(message.from_user.id, "I love you too <3")
    else:
        bot.send_message(message.from_user.id, "meow ^ ^")


bot.add_custom_filter(custom_filters.StateFilter(bot))
bot.infinity_polling(skip_pending=True)

