import json
import os

ROW = 9

if not os.path.exists(f"posibilities.json"):
    with open(f"posibilities.json", "w") as f:
        json.dump({}, f)


def collect_ith_characters(strings):
    # Assume all strings are of the same length, here length 11
    length_of_strings = 11
    # Create a list of sets for each position
    character_sets = [set() for _ in range(length_of_strings)]

    # Iterate over each string in the list
    for s in strings:
        # For each string, update the set corresponding to each position
        for i in range(length_of_strings):
            character_sets[i].add(s[i])

    out = []
    for c in character_sets:
        out.append("".join(list(c)))
    return out


with open(f"row_{ROW}.json") as f:
    good_strings = json.load(f)

vals = collect_ith_characters(good_strings)
print(json.dumps(vals, indent=1))
with open(f"posibilities.json") as f:
    data = json.load(f)

data[str(ROW)] = vals
with open(f"posibilities.json", "w") as f:
    json.dump(data, f)
