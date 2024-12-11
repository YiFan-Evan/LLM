import os
import json

remove_list = []

for dirpath, dirnames, filenames in os.walk('.'):
    for filename in filenames:
        f = open(os.path.join(dirpath, filename), 'r')
        str = f.read()
        if '[{"role": "system"' in str and filename.endswith('.json'):
            remove_list.append(os.path.join(dirpath, filename))

for file in remove_list:
    os.remove(file)
