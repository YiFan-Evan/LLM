import os
import json

MODEL = "gpt-4o-2024-05-13"
MODE = "space"
TASK = "T2"

path = rf"../../../../Result/{MODEL}/{MODE}/{TASK}"

total = 0
correct = 0

for dirpath, dirnames, filenames in os.walk(path):
    for filename in filenames:
        if filename.endswith(".json"):
            f = open(os.path.join(dirpath, filename), "r")
            data = json.load(f)
            question1 = data[1]["content"].split("Starting from the ")[1].split(", you move around the ring by ")[0]
            answer2 = data[4]["content"]
            if question1 == answer2:
                correct += 1
            total += 1
print(correct/total)

f = open("eval.txt", "w")
f.write(str(correct/total))
f.close()