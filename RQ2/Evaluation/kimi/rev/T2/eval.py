import os
import json

MODEL = "kimi"
MODE = "rev"
TASK = "T2"

path = rf"../../../../Result/{MODEL}/{MODE}/{TASK}"

total = 0
correct = 0

for dirpath, dirnames, filenames in os.walk(path):
    for filename in filenames:
        if filename.endswith(".json"):
            f = open(os.path.join(dirpath, filename), "r")
            data = json.load(f)
            answer1 = data[2]["content"].split("->")
            print(answer1)
            answer2 = data[4]["content"].split("->")
            print(answer2)
            try:
                flag = True
                for i in range(len(answer1)):
                    if answer1[i] != answer2[len(answer2) - 1 - i]:
                        flag = False
                if flag:
                    correct += 1
            except Exception as e:
                print(e)
                continue
            total += 1
print(correct / total)

f = open("eval.txt", "w")
f.write(str(correct/total))
f.close()