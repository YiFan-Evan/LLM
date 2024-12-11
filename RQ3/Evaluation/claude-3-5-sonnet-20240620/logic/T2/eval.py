import os
import json

MODEL = "gpt-3.5-turbo"
MODE = "logic"
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
                    peace = data[2]["content"].split(">")[1].strip().replace("(", "").replace(")", "").strip()
                except:
                    continue
                answer1 = answer1.split("-")[0].strip().replace("(", "").replace(")", "").strip().split(",")
                answer2 = answer2.split("-")[0].strip().replace("(", "").replace(")", "").strip().split(",")
                try:
                    if sum(list(map(int, answer1))) == sum(list(map(lambda x:int(peace)-int(x), answer2))):
                        correct += 1
                except:
                    continue
                total += 1
    print(f"PROMPT: {PROMPT}", end=" ")
    print(correct/total)

    f = open("eval.txt", "w")
    f.write(str(correct/total))
    f.close()