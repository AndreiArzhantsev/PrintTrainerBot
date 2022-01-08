import sys
import time
from get_text import GetText
from accuracy import Accuracy

def PrintWithSleep(string, sleep_time):
    print(string)
    time.sleep(sleep_time)

orig_text = GetText();

PrintWithSleep("Are you ready?", 1)
PrintWithSleep(orig_text, 2)
PrintWithSleep("3", 0.5)
PrintWithSleep("2", 0.5)
PrintWithSleep("1", 0.5)
print("Start")
start_time = time.time()

your_text = ''
while((c := sys.stdin.read(1)) != '' and c != '\n'):
    your_text += c

end_time = time.time()

print("You made", Accuracy(orig_text, your_text) - 1, "typos")
print("Your accuracy is: ", 100 - 100 * (Accuracy(orig_text, your_text) - 1) / len(orig_text), "%", sep='')
print("Time spent:", end_time - start_time)

