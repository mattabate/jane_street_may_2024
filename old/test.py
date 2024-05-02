import json

with open("merge_89.json") as f:
    merge_89 = json.load(f)


new_9 = []
for k in merge_89.keys():
    new_9.extend(merge_89[k])

new_9 = list(set(new_9))

with open("row_9_new.json", "w") as f:
    json.dump(new_9, f)
