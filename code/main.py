import sys
import time
from get_text import GetText

def PrintWithSleep(string, sleep_time):
    print(string)
    time.sleep(sleep_time)

orig_text = GetText();


def Accuracy(pattern, result):
    len1 = len(pattern)
    len2 = len(result)
    penalty = [[0 for j in range(len2+1)] for i in range(len1+1)]
    for i in range (len1+1):
        penalty[i][0] = i   
    for j in range (len2+1):
        penalty[0][j] = j
    for i in range(1, len1+1):
        for j in range(1, len2+1):
            same = (pattern[i-1] != result[j-1])
            penalty[i][j] = min(penalty[i][j-1]+1, min(penalty[i-1][j]+1, penalty[i-1][j-1]+same))
    return penalty[len1][len2]


PrintWithSleep("Are you ready?", 1)
PrintWithSleep(orig_text, 0.5)
PrintWithSleep("3", 0.5)
PrintWithSleep("2", 0.5)
PrintWithSleep("1", 0.5)
print("Start")
start_time = time.time()

your_text = ''
c = ''
while(c != '\n'):
    your_text += c
    c = sys.stdin.read(1)

end_time = time.time()

if (orig_text == your_text):
    print("Well done")
else:
    print("Practice more kid")
print("Accuracy", Accuracy(orig_text, your_text))
print("Time spent", end_time - start_time)

