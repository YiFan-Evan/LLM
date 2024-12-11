import os
import json

MODEL = "qwen"
MODE = "logic"
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
                answer2 = data[4]["content"]
                if "Therefore, the final answer is:" in answer2:
                    answer2 = answer2.split("Therefore, the final answer is:")[1].strip()
                answer1 = answer1.split("-")[0].strip().replace("(", "").replace(")", "").strip().split(",")
                answer2 = answer2.split("-")[0].strip().replace("(", "").replace(")", "").strip().split(",")
                try:
                    if sum(list(map(lambda x:int(x)+1, answer1))) == sum(list(map(int, answer2)))-1:
                        correct += 1
                    total += 1
                except:
                    continue
    print(f"PROMPT: {PROMPT}", end=" ")
    print(correct/total)

    f = open("eval.txt", "w")
    f.write(str(correct/total))
    f.close()