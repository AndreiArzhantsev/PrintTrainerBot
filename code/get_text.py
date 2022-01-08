import random
import os

def GetText(lang, difficulty):
    if difficulty == "1":
        min_size = 20
        max_size = 50
    elif difficulty == "2":
        min_size = 50
        max_size = 100
    elif difficulty == "3":
        min_size = 100
        max_size = 200

    if lang == "1":
        DIR = '../src/eng'
    elif lang == "2":
        DIR = '../src/rus'
    source = open(os.path.join(DIR, random.choice(os.listdir(DIR))))
    text = source.readlines()
    while True:
        pattern = text[random.randrange(len(text))]
        # pattern.split() in line below seems to be replaced with smth better
        if min_size <= len(pattern.split(' ')) <= max_size:
            return pattern

