import os
import json

MODEL = "kimi"
MODE = "image"
TASK = "T2"

path = rf"../../../../Result/{MODEL}/{MODE}/{TASK}"

total = 0
correct = 0

for dirpath, dirnames, filenames in os.walk(path):
    for filename in filenames:
        if filename.endswith(".json"):
            f = open(os.path.join(dirpath, filename), "r")
            data = json.load(f)
            print(data[2]["content"])
            print(data[4]["content"])
            answer11 = data[2]["content"].split(":")[1].split(" ")[0]
            answer12 = data[2]["content"].split(":")[2].strip()
            answer21 = data[4]["content"].split(":")[1].split(" ")[0]
            answer22 = data[4]["content"].split(":")[2].strip()
            if answer11==answer22 and answer12==answer21:
                correct += 1
            total += 1
print(correct/total)

f = open("eval.txt", "w")
f.write(str(correct/total))
f.close()