import os
import json
path = rf"."

for dirpath, dirnames, filenames in os.walk(path):
    for filename in filenames:
        if filename.endswith(".json"):
            f = open(os.path.join(dirpath, filename), "r")
            data = json.load(f)
            #remove data[1]
            data.pop(1)
            g = open(os.path.join(dirpath, filename), "w")
            json.dump(data, g)
            g.close()
            f.close()
