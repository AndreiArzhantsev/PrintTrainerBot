import random
import os


def GetSource(lang):
    if lang == "1":
        return '../src/eng/'
    elif lang == "2":
        return '../src/rus/'


def GetText(source, size):
    if size == "1":
        source += 'short/'
    elif size == "2":
        source += 'medium/'
    elif size == "3":
        source += 'long/'
    path = os.path.join(source, random.choice(os.listdir(source)))
    text = open(path, 'r').readlines()
    return text[random.randrange(len(text))], path.split('/')[4][:-4]

