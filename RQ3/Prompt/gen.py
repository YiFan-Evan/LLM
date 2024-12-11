import json
import os

for dirpath, dirnames, filenames in os.walk("../Prompt"):
    for filename in filenames:
        if filename.endswith(".txt") and 'example' in dirpath:
            prompt = "(Here is an example: "
            names = dirpath.split("\\")
            f = open(f"../../RQ1/Result/claude-3-5-sonnet-20240620/{names[-2]}/{names[-1]}/150.json", "r")
            data = json.load(f)
            data.remove(data[0])
            prompt += str(data) + ")"
            f.close()
            f = open(os.path.join(dirpath, filename), "w")
            f.write(prompt)
            f.close()
        elif filename.endswith(".txt") and 'knowledge' in dirpath:
        #     prompt = "(Notice that "
        #     f = open(os.path.join(dirpath, filename), "w")
        #     f.write(prompt)
        #     f.close()
            pass
        elif filename.endswith(".txt") and 'five' in dirpath:
            prompt = "(Here are five examples: "
            names = dirpath.split("\\")
            f = open(f"../../RQ1/Result/claude-3-5-sonnet-20240620/{names[-2]}/{names[-1]}/150.json", "r")
            data = json.load(f)
            data.remove(data[0])
            prompt += "1. " + str(data) + ", "
            f.close()
            f = open(f"../../RQ1/Result/claude-3-5-sonnet-20240620/{names[-2]}/{names[-1]}/151.json", "r")
            data = json.load(f)
            data.remove(data[0])
            prompt += "2. " + str(data) + ", "
            f.close()
            f = open(f"../../RQ1/Result/claude-3-5-sonnet-20240620/{names[-2]}/{names[-1]}/152.json", "r")
            data = json.load(f)
            data.remove(data[0])
            prompt += "3. " + str(data) + ", "
            f.close()
            f = open(f"../../RQ1/Result/claude-3-5-sonnet-20240620/{names[-2]}/{names[-1]}/153.json", "r")
            data = json.load(f)
            data.remove(data[0])
            prompt += "4. " + str(data) + ", "
            f.close()
            f = open(f"../../RQ1/Result/claude-3-5-sonnet-20240620/{names[-2]}/{names[-1]}/154.json", "r")
            data = json.load(f)
            data.remove(data[0])
            prompt += "5. " + str(data) + ")"
            f.close()
            f = open(os.path.join(dirpath, filename), "w")
            f.write(prompt)
            f.close()
        elif filename.endswith(".txt") and 'cot' in dirpath:
            prompt = "(For each problem, you need to provide your thought process and ultimately present the conclusion in the form of \"Therefore, the final answer is: \")"
            f = open(os.path.join(dirpath, filename), "w")
            f.write(prompt)
            f.close()
        elif filename.endswith(".txt") and 'analogical' in dirpath:
            prompt = "(For each problem, you need to first present three related but not identical problems, along with a description of each problem and its solution. Finally, provide the answer to the original problem in the form of \"Therefore, the final answer is: \".)"
            f = open(os.path.join(dirpath, filename), "w")
            f.write(prompt)
            f.close()
        elif filename.endswith(".txt") and 'back' in dirpath:
            prompt = "(For each problem, you need to first explain the fundamental principles involved in solving it, and then provide the answer to the problem in the form of \"Therefore, the final answer is: \".)"
            f = open(os.path.join(dirpath, filename), "w")
            f.write(prompt)
            f.close()