import sys
import time
from get_text import GetText
from accuracy import Accuracy

def PrintWithSleep(string, sleep_time):
    print(string)
    time.sleep(sleep_time)

# where main starts
###########################################################################

# choosing language
print("Select the text language:", "1: English", "2: Русский", sep='\n')
lang = ""
while (lang := input()) not in {"1", "2"}:
    print("Please select 1 or 2")

# choosing difficulty
print("Select the size of the text:", "1: 20-50 words", "2: 50-100 words", "3: 100-200 words", sep='\n')
difficulty = ""
while (difficulty := input()) not in {"1", "2", "3"}:
    print("Please select 1 or 2 or 3")

# competition starts there!
orig_text = GetText(lang, difficulty)

PrintWithSleep("Are you ready?", 1)
PrintWithSleep(orig_text, 1.5)
PrintWithSleep("3", 0.5)
PrintWithSleep("2", 0.5)
PrintWithSleep("1", 0.5)
print("Start")
start_time = time.time()

your_text = ''
while (c := sys.stdin.read(1)) != '\n':
    your_text += c

end_time = time.time()

accuracy_result = Accuracy(orig_text.strip(), your_text.strip())
print("You made", accuracy_result, "typos")
print("Your accuracy is: ", 100 - 100 * accuracy_result / len(orig_text), "%", sep='')
print("Time spent:", end_time - start_time)

# where main ends
###########################################################################

