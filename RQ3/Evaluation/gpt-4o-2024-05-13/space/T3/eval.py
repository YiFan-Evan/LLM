import os
import json

MODEL = "gpt-4o-2024-05-13"
MODE = "space"
TASK = "T3"

path = rf"../../../../Result/{MODEL}/{MODE}/{TASK}"

total = 0
correct = 0

for dirpath, dirnames, filenames in os.walk(path):
    for filename in filenames:
        if filename.endswith(".json"):
            f = open(os.path.join(dirpath, filename), "r")
            data = json.load(f)
            question1 = data[1]["content"]
            step = question1.split("You have been given a circular path consisting of ")[1].split(
                " connected dots. At the start, you are positioned on")[0]
            question1_place = question1.split("Starting from the ")[1].split(", you move around the ring by ")[0]
            answer1 = data[2]["content"]
            question2 = data[3]["content"]
            question2_place = question2.split("Starting from the ")[1].split(", you move around the ring by ")[0]
            answer2 = data[4]["content"]
            things = question1.split('Moving in a clockwise direction from ')[1].split(
                '. Starting from the ')[0]
            things = things.replace("elements on the path are ", "") \
                .replace(" an ", " | ").replace(" a ", " | ") \
                .replace(" and ", " | ").replace(",and ", ",| ") \
                .replace(" the ", " | ").replace(",the ", ",| ") \
                .replace("| ", "").replace("the ", "") \
                .replace(", ", ",")
            things_list = things.split(",")
            print(question1)
            print(answer1)
            print(question2)
            print(answer2)
            print(things_list)
            question_index = 0
            answer1_index = 0
            answer2_index = 0
            i = 1
            for item in things_list:
                if item == question1_place.lower():
                    question_index = i
                if item == answer1.lower():
                    answer1_index = i + int(step)
                if item == answer2.lower():
                    answer2_index = i + 2 * int(step)
                i += 1
            if (answer2_index - answer1_index) % int(step) == (answer1_index - question_index) % int(step):
                correct += 1
            total += 1
print(correct / total)

f = open("eval.txt", "w")
f.write(str(correct / total))
f.close()
