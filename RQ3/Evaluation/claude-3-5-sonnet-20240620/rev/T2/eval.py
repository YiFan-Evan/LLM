import os
import json

MODEL = "gpt-3.5-turbo"
MODE = "rev"
TASK = "T2"


PROMPTS = ["knowledge","example","five","cot","back","analogical"]
for PROMPT in PROMPTS:
    path = rf"../../../../Result/{MODEL}/{PROMPT}/{MODE}/{TASK}"

    total = 0
    correct = 0

    for dirpath, dirnames, filenames in os.walk(path):
        for filename in filenames:
            if filename.endswith(".json"):
                f = open(os.path.join(dirpath, filename), "r")
                data = json.load(f)
                answer1 = data[2]["content"]
                if "Therefore, the final answer is:" in answer1:
                    answer1 = answer1.split("Therefore, the final answer is:")[1].strip()
                answer1 =answer1.split("->")
                answer2 = data[4]["content"]
                if "Therefore, the final answer is:" in answer2:
                    answer2 = answer2.split("Therefore, the final answer is:")[1].strip()
                answer2 =answer2.split("->")
                try:
                    flag = True
                    for i in range(len(answer1)):
                        if answer1[i] != answer2[len(answer2) - 1 - i]:
                            flag = False
                    if flag:
                        correct += 1
                except Exception as e:
                    #print(e)
                    continue
                total += 1
    print(f"PROMPT: {PROMPT}", end=" ")
    print(correct / total)

    f = open("eval.txt", "w")
    f.write(str(correct/total))
    f.close()