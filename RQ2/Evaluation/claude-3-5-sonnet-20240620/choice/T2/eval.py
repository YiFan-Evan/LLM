import os
import json

MODEL = "claude-3-5-sonnet-20240620"
MODE = "choice"
TASK = "T2"

path = rf"../../../../Result/{MODEL}/{MODE}/{TASK}"

total = 0
correct = 0

for dirpath, dirnames, filenames in os.walk(path):
    for filename in filenames:
        if filename.endswith(".json"):
            f = open(os.path.join(dirpath, filename), "r")
            data = json.load(f)
            answer1 = data[2]["content"].strip()
            print(answer1)
            answer2 = data[4]["content"].strip()
            print(answer2)
            try:
                if ord(answer1) + ord(answer2) == ord("C") + ord("C"):
                    correct += 1
            except:
                continue
            total += 1
print(correct/total)

f = open("eval.txt", "w")
f.write(str(correct/total))
f.close()