import os
import json

from Tools.scripts.finddiv import process
from Tools.scripts.fixnotice import process


def only_numbers(s):
    digit = ['0','1','2','3','4','5','6','7','8','9','.','-']
    new_str=""
    for i in s:
        if i in digit:
            new_str+=i
        else:
            new_str+=" "
    return new_str

def get_last_number(s):
    digit = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '.', '-']
    num = ""
    for i in range(len(s)-1,-1,-1):
        if s[i] in digit:
            num = s[i]+num
        else:
            if num!="" and num!="." and num!="-":
                return num

def remove_last_dot(s):
    if s is None:
        return None
    while s[-1]=="." or s[-1]=="-":
        s = s[:-1]
        if s == "":
            return None
    return s

def process(s):
    return remove_last_dot(get_last_number(only_numbers(s)))
MODEL = "gpt-4o-2024-05-13"
MODE = "math"
TASK = "T3"

path = rf"../../../../Result/{MODEL}/{MODE}/{TASK}"

total = 0
correct = 0

for dirpath, dirnames, filenames in os.walk(path):
    for filename in filenames:
        if filename.endswith(".json"):
            f = open(os.path.join(dirpath, filename), "r")
            data = json.load(f)
            answer1 = process(data[2]["content"])
            print(answer1)
            answer2 = process(data[4]["content"])
            print(answer2)
            try:
                if int(answer1)+8==int(answer2):
                    correct += 1
            except:
                continue
            total += 1
print(correct/total)

f = open("eval.txt", "w")
f.write(str(correct/total))
f.close()