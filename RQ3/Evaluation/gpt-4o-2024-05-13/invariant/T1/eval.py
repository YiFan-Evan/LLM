import os
import json

MODEL = "gpt-4o-2024-05-13"
MODE = "invariant"
TASK = "T1"

path = rf"../../../../Result/{MODEL}/{MODE}/{TASK}"

total = 0
correct = 0

for dirpath, dirnames, filenames in os.walk(path):
    for filename in filenames:
        if filename.endswith(".json"):
            f = open(os.path.join(dirpath, filename), "r")
            data = json.load(f)
            answer1 = data[2]["content"]
            print(answer1)
            answer2 = data[4]["content"]
            print(answer2)
            if answer1==answer2:
                correct += 1
            total += 1
print(correct/total)

f = open("eval.txt", "w")
f.write(str(correct/total))
f.close()