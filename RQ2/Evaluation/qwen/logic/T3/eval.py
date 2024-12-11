import os
import json

MODEL = "qwen"
MODE = "logic"
TASK = "T3"

path = rf"../../../../Result/{MODEL}/{MODE}/{TASK}"

total = 0
correct = 0

for dirpath, dirnames, filenames in os.walk(path):
    for filename in filenames:
        if filename.endswith(".json"):
            f = open(os.path.join(dirpath, filename), "r")
            data = json.load(f)
            answer1 = data[2]["content"].split("-")[0].strip().replace("(", "").replace(")", "").strip().split(",")
            print(answer1)
            answer2 = data[4]["content"].split("-")[0].strip().replace("(", "").replace(")", "").strip().split(",")
            print(answer2)
            try:
                if sum(list(map(lambda x:int(x)+1, answer1))) == sum(list(map(int, answer2)))-1:
                    correct += 1
            except Exception as e:
                print(e)
                continue
            total += 1
print(correct/total)

f = open("eval.txt", "w")
f.write(str(correct/total))
f.close()