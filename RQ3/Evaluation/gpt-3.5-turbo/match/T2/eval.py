import os
import json

MODEL = "claude-3-5-sonnet-20240620"

path = rf"..\..\..\..\Result\{MODEL}\match\T2"

total = 0
correct = 0

for dirpath, dirnames, filenames in os.walk(path):
    for filename in filenames:
        if filename.endswith(".json"):
            f = open(os.path.join(dirpath, filename), "r")
            data = json.load(f)
            answer1 = data[2]["content"]
            answer2 = data[4]["content"]
            if int(answer1)*2==int(answer2):
                correct += 1
            total += 1
print(correct/total)

f = open("eval.txt", "w")
f.write(str(correct/total))
f.close()