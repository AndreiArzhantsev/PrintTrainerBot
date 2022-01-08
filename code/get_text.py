import random

def GetText():
    source = open('../src/potter.txt', 'r')
    text = source.readlines()
    print("Select the size of the text:")
    print("1: 20-50 words")
    print("2: 50-100 words")
    print("3: 100-200 words")
    ans = input()
    if ans == "1":
        min_size = 20
        max_size = 50
    elif ans == "2":
        min_size = 50
        max_size = 100
    elif ans == "3":
        min_size = 100
        max_size = 200
    else:
        raise 'Do not fool me'
    while True:
        pattern = text[random.randrange(len(text))]
        if min_size <= len(pattern.split(' ')) <= max_size:
            return pattern
        
