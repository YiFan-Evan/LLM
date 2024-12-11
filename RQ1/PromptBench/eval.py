import numpy as np

for i in range(1,4):
    for j in range(1,5):
        f = open(f"./test-t5{i}{j}.txt", encoding="utf-8")
        T_acc = []
        ori = []
        post = []
        PDR = []
        ori_acc = 0
        for line in f:
            if "T accuracy:" in line:
                T_acc.append(float(line.split(":")[1].strip()))
            if "Current accuracy-o is:" in line:
                ori_acc = float(line.split(":")[1].strip())
            if "Current accuracy is:" in line:
                post.append(float(line.split(":")[1].strip()))
            PDR = [1 - (ori_acc - post[i]) for i in range(len(post))]
        print(f"T5{i}{j}: T_acc: {np.mean(T_acc)}, ori: {ori_acc}, post: {np.mean(post)}, PDR: {np.mean(PDR)}")