import os
for lang in ['eng', 'rus']:
    path = '../src/' + lang + '/raw/'
    short = '../src/' + lang + '/short/'
    medium = '../src/' + lang + '/medium/'
    long = '../src/' + lang + '/long/'

    file_list = os.listdir(path)
    for f in file_list:
        text = open(os.path.join(path + f), 'r').readlines()
        for line in text:
            cwords = len(line.split(' '))
            if 20 <= cwords < 50:
                where = open(os.path.join(short + f), 'a')
                where.write(line)
            elif 50 <= cwords < 100:
                where = open(os.path.join(medium + f), 'a')
                where.write(line)
            elif 100 <= cwords < 200:
                where = open(os.path.join(long + f), 'a')
                where.write(line)

