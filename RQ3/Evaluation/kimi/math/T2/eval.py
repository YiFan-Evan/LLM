import os
import json

MODEL = "kimi"
MODE = "math"
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
                answer2 = data[4]["content"]
                if "Therefore, the final answer is:" in answer2:
                    answer2 = answer2.split("Therefore, the final answer is:")[1].strip()
                try:
                    if 5*int(answer1)==int(answer2):
                        correct += 1
                except:
                    continue
                total += 1
    print(f"PROMPT: {PROMPT}", end=" ")
    print(correct/total)

    f = open("eval.txt", "w")
    f.write(str(correct/total))
    f.close()