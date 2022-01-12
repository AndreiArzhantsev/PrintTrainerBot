import os


for lang in ['eng', 'rus']:
    path = '../src/' + lang + '/raw/'
    short = '../src/' + lang + '/short/'
    medium = '../src/' + lang + '/medium/'
    long = '../src/' + lang + '/long/'

    file_list = os.listdir(path)
    for f in file_list:
        text = open(os.path.join(path + f), 'r').readlines()
        where_short = open(os.path.join(short + f), 'w')
        where_medium = open(os.path.join(medium + f), 'w')
        where_long = open(os.path.join(long + f), 'w')
        for line in text:
            cwords = len(line.split(' '))
            if 20 <= cwords < 50:
                where_short.write(line)
            elif 50 <= cwords < 100:
                where_medium.write(line)
            elif 100 <= cwords < 200:
                where_long.write(line)

