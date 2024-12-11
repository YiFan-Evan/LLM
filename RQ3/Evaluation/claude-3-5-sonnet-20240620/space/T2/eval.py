import os
import json

MODEL = "gpt-3.5-turbo"
MODE = "space"
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
                question1 = data[1]["content"].split("Starting from the ")[1].split(", you move around the ring by ")[0]
                answer2 = data[4]["content"]
                if "Therefore, the final answer is:" in answer2:
                    answer2 = answer2.split("Therefore, the final answer is:")[1].strip()
                if question1 == answer2:
                    correct += 1
                total += 1
    print(f"PROMPT: {PROMPT}", end=" ")
    print(correct/total)

    f = open("eval.txt", "w")
    f.write(str(correct/total))
    f.close()