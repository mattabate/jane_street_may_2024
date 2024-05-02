import json
import tqdm


with open("row_9.json") as f:
    strings_set1 = json.load(f)
with open("row_10.json") as f:
    strings_set2 = json.load(f)

col_rol = [1, 0, 1, 0, 0, 0, 1, 1, 1, 1, 0]

out = {}
for s1 in tqdm.tqdm(strings_set1):
    out[s1] = []
    for s2 in strings_set2:
        for i in range(11):
            if s1[i] == "x" and s2[i] == "x":
                break  # bad
            if s1[i] == "x" or s2[i] == "x" or col_rol[i] == 0:
                continue
            if s1[i] != s2[i]:
                break
        else:
            out[s1].append(s2)

    if not out[s1]:
        del out[s1]

with open("merge_910.json", "w") as f:
    json.dump(out, f)


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


print("row 9")
new_row_9 = [x for x in out.keys()]
print(json.dumps(collect_ith_characters(out.keys()), indent=1))

print("row 10")
new_row_10 = []
for k in out.keys():
    new_row_10.extend(out[k])
new_row_10 = list(set(new_row_10))
print(json.dumps(collect_ith_characters(new_row_10), indent=1))

with open("10_vals.json", "w") as f:
    json.dump(collect_ith_characters(new_row_10), f)


with open("row_9.json", "w") as f:
    json.dump(new_row_9, f)

with open("row_10.json", "w") as f:
    json.dump(new_row_10, f)
