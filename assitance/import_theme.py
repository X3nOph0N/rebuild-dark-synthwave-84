import json
from json import load,dump
with open('./synthwave-color-theme.json','rt',encoding='utf-8') as f:
    new = load(f)
with open('./old.json','rt',encoding='utf-8') as f:
    old = load(f)

skip = ["name","type","semanticHighlighting"]
colors = "colors"
tokenColors = "tokenColors"

for key in old:
    if old in skip:
        continue
    elif key == colors:
        ...
        for key_1 in new[key]:
            try:
                new[key][key_1] = old[key][key_1]
            except KeyError:
                ...
                # new[key][key_1] = None
    elif key == tokenColors:
        for item,i in zip(new[key],range(len(new[key]))):
            for key_1 in item:
                if key_1 == "settings":
                    for key_2 in item:
                        try:
                            item[key_2] = old[key][i][key_2]
                        except:
                            ...
with open('./new.json','wt') as f:
    dump(new,f)
