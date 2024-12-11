import csv
import os

content = ["choice","image","invariant","logic","math","rev","space"]

path = "../../RQ1/Dataset"

assert os.path.exists(path)

data = "../../RQ1/Dataset/choice/base.csv"

reader = csv.reader(open(data, "r", encoding="GBK"), delimiter="|")
labels = []

for i, row in enumerate(reader):
    ans = row[1].replace("[\"", "").replace("'\"]", "").replace(" \" '", "").replace("'\"", "")
    ans = list(ans.split(","))
    label = row[2].replace(" '", "").replace("'", "").strip().replace('friends house',
                                                                      'friend\'s house').replace(
        'youre curious', 'you\'re curious')
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
for i in range(150,155):
    print(labels[i])
data = "../../RQ1/Dataset/image/base.csv"

reader = csv.reader(open(data, "r",encoding="GBK"))
labels = []

for i, row in enumerate(reader):
    labels.append(row)
for i in range(150,155):
    print(labels[i])
data = "../../RQ1/Dataset/invariant/ans.csv"

reader = csv.reader(open(data, "r",encoding="GBK"), delimiter="|")
labels = []

for i, row in enumerate(reader):
    labels.append(row)
for i in range(150,155):
    print(labels[i])
data = "../../RQ1/Dataset/logic/ans.csv"

reader = csv.reader(open(data, "r",encoding="GBK"), delimiter="|")
labels = []

for i, row in enumerate(reader):
    labels.append(row)
for i in range(150,155):
    print(labels[i])
data = "../../RQ1/Dataset/math/ans.csv"

reader = csv.reader(open(data, "r",encoding="GBK"), delimiter="|")
labels = []

for i, row in enumerate(reader):
    labels.append(row)
for i in range(150,155):
    print(labels[i])
data = "../../RQ1/Dataset/rev/ans.csv"

reader = csv.reader(open(data, "r",encoding="GBK"))
labels = []

for i, row in enumerate(reader):
    labels.append(row[0].split("|")[1] if "|" in row[0] else row[0])
for i in range(150,155):
    print(labels[i])
data = "../../RQ1/Dataset/space/ans.csv"

reader = csv.reader(open(data, "r",encoding="GBK"), delimiter="|")
labels = []

for i, row in enumerate(reader):
    labels.append(row)
for i in range(150,155):
    print(labels[i])