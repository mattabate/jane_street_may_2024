import json

ROW = 10

with open(f"row_{ROW}.json") as f:
    rows = json.load(f)

chars = ["" for _ in range(11)]

for i in range(11):
    for row in rows:
        if row[i] not in chars[i]:
            chars[i] += row[i]

print(chars)
