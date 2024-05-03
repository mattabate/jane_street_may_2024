import json

ROW = 9

with open("row_8.json") as f:
    rows = json.load(f)

chars = ["" for _ in range(11)]

for i in range(11):
    for row in rows:
        if row[i] not in chars[i]:
            chars[i] += row[i]

print(chars)
