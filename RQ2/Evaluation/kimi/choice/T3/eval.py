import os
import json
import csv

MODEL = "kimi"
MODE = "choice"
TASK = "T3"

path = rf"../../../../Result/{MODEL}/{MODE}/{TASK}"

data = "../../../../../RQ1/Dataset/choice/base.csv"

reader = csv.reader(open(data, "r",encoding="GBK"), delimiter="|")
labels = []

for i, row in enumerate(reader):
    ans = row[1].replace("[\"", "").replace("'\"]", "").replace(" \" '", "").replace("'\"", "")
    ans = list(ans.split(","))
    label = row[2].replace(" '", "").replace("'", "").strip().replace('friends house', 'friend\'s house').replace('youre curious',  'you\'re curious')
    print(ans)
    print(label)
    if label == 'practise':
        print("i=", i)
    if label == ans[0]:
        labels.append("A")
    elif label == ans[1]:
        labels.append("B")
    elif label == ans[2]:
        labels.append("C")
    elif label == ans[3]:
        labels.append("D")
    elif label == ans[4]:
        labels.append("E")
    else:
        print("error")

total = 0
correct = 0
print(len(labels))
for dirpath, dirnames, filenames in os.walk(path):
    for filename in filenames:
        if filename.endswith(".json"):
            i = int(filename.split(".")[0])
            f = open(os.path.join(dirpath, filename), "r")
            data = json.load(f)
            answer1 = data[2]["content"]
            answer2 = data[4]["content"]
            label = labels[i]
            print(f"i: {i}")
            print(f"label: {label}, answer1: {answer1}, answer2: {answer2}")
            if answer2==label:
                correct += 1
            total += 1
print(correct/total)

f = open("eval.txt", "w")
f.write(str(correct/total))
f.close()