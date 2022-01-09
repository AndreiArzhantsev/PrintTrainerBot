import random
import os
import re


def GetSource(lang):
    if lang == "1":
        DIR = './src/eng'
    elif lang == "2":
        DIR = './src/rus'
    return os.path.join(DIR, random.choice(os.listdir(DIR)))


def GetText(source, difficulty):
    source = open(source)

    if difficulty == "1":
        min_size = 20
        max_size = 50
    elif difficulty == "2":
        min_size = 50
        max_size = 100
    elif difficulty == "3":
        min_size = 100
        max_size = 200

    text = source.readlines()
    while True:
        pattern = text[random.randrange(len(text))]
        # pattern.split() in line below seems to be replaced with smth better
        if min_size <= len(pattern.split(' ')) <= max_size:
            return pattern


def NameOfTheBook(source):
    source = source.replace('/', '.')
    return source.split('.')[4]
