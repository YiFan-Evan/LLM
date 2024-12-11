import os
import json

MODEL = "kimi"
MODE = "invariant"
TASK = "T3"

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
            index = chr(int(filename.split(".")[0])%20+ord('a'))
            if (answer1.replace("0",index)
                    .replace(f"{index}-1","len(arr)-1")==answer2):
                correct += 1
            total += 1
print(correct/total)

f = open("eval.txt", "w")
f.write(str(correct/total))
f.close()