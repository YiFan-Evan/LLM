import os
import json

MODEL = "gpt-3.5-turbo"
MODE = "rev"
TASK = "T3"
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
                if answer1[-4] == "-":
                    answer1 = answer1[:-1]
                answer2 = data[4]["content"]
                if "Therefore, the final answer is:" in answer2:
                    answer2 = answer2.split("Therefore, the final answer is:")[1].strip()
                if answer1[:-3]==answer2:
                    correct+=1
                total += 1
    print(f"PROMPT: {PROMPT}", end=" ")
    print(correct / total)

    f = open("eval.txt", "w")
    f.write(str(correct/total))
    f.close()