import os
import json

MODEL = "o1-mini-2024-09-12"
MODE = "math"
TASK = "T2"

path = rf"../../../../Result/{MODEL}/{MODE}/{TASK}"

total = 0
correct = 0

for dirpath, dirnames, filenames in os.walk(path):
    for filename in filenames:
        if filename.endswith(".json"):
            f = open(os.path.join(dirpath, filename), "r")
            data = json.load(f)
            answer1 = data[3]["content"]
            print(answer1)
            answer2 = data[5]["content"]
            print(answer2)
            try:
                if 5*int(answer1)==int(answer2):
                    correct += 1
            except:
                continue
            total += 1
print(correct/total)

f = open("eval.txt", "w")
f.write(str(correct/total))
f.close()