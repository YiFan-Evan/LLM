import os
import json

MODEL = "claude-3-5-sonnet-20240620"
MODE = "logic"
TASK = "T2"

path = rf"../../../../Result/{MODEL}/{MODE}/{TASK}"

total = 0
correct = 0

for dirpath, dirnames, filenames in os.walk(path):
    for filename in filenames:
        if filename.endswith(".json"):
            f = open(os.path.join(dirpath, filename), "r")
            data = json.load(f)
            try:
                peace = data[2]["content"].split(">")[1].strip().replace("(", "").replace(")", "").strip()
            except:
                continue
            answer1 = data[2]["content"].split("-")[0].strip().replace("(", "").replace(")", "").strip().split(",")
            print(answer1)
            answer2 = data[4]["content"].split("-")[0].strip().replace("(", "").replace(")", "").strip().split(",")
            print(answer2)
            try:
                if sum(list(map(int, answer1))) == sum(list(map(lambda x:int(peace)-int(x), answer2))):
                    correct += 1
            except:
                continue
            total += 1
print(correct/total)

f = open("eval.txt", "w")
f.write(str(correct/total))
f.close()