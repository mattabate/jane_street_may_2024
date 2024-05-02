import itertools
import tqdm
import json

row = [0, 1, 1, 1, 1, 0, 1, 0, 1, 1]


def does_string_fit_row(s: str, row: list):
    if len(s) != 11:
        raise ValueError("String must be of length 11")
    if len(row) != 10:
        raise ValueError("Row must be of length 10")

    if "xx" in s:
        return False

    for j in range(10):
        if "x" not in s[j : j + 1]:
            if row[j] == 0 and s[j] != s[j + 1]:
                return False
            if row[j] == 1 and s[j] == s[j + 1]:
                return False

    return True


# Define the character sets for the different positions
set1 = "1379x"
set2 = "0123456789x"  # Characters for positions 0, 2, 5, 7

# length 5 for "1379x"
strings_set1 = ["".join(p) for p in itertools.product(set1, repeat=5)]
# len 6 for set "0123456789x"
strings_set2 = ["".join(p) for p in itertools.product(set2, repeat=6)]

new_set1 = []
for s in strings_set1:
    if s[0] == "x":
        continue

    if "x" == s[1] == s[2] or "x" == s[2] == s[3] or "x" == s[3] == s[4]:
        continue

    if s[3] != "x" and s[4] != "x" and s[3] != s[4]:
        continue
    new_set1.append(s)
strings_set1 = new_set1  # places 2 5 7 9 11
strings_set1[0] = strings_set1[0].replace("x", "")

new_set2 = []
for s in strings_set2:
    if s[0] == "0" or s[5] == "x":
        continue

    if (
        "x" == s[0] == s[1]
        or "x" == s[2] == s[3]
        or "x" == s[3] == s[4]
        or "x" == s[4] == s[5]
    ):
        continue

    if s[1] != "x" and s[2] != "x" and s[1] == s[2]:
        continue

    if s[1] == "x" and s[2] == "0":
        continue
    new_set2.append(s)
strings_set2 = new_set2  # any value, places 1 3 4 6 8 10


print("Total strings in set1:", len(strings_set1))
print("Total strings in set2:", len(strings_set2))
print("Total in Merged:", len(strings_set1) * len(strings_set2))


# Function to merge strings from set1 and set2 into the final format
def merge_strings(set1_str, set2_str):
    return (
        set2_str[0]
        + set1_str[0]
        + set2_str[1]
        + set2_str[2]
        + set1_str[1]
        + set2_str[3]
        + set1_str[2]
        + set2_str[4]
        + set1_str[3]
        + set2_str[5]
        + set1_str[4]
    )


# List to hold all possible combined strings
final_strings = []

# Combine every string from set1 with every string from set2
for s1 in tqdm.tqdm(strings_set1):
    for s2 in strings_set2:
        sm = merge_strings(s1, s2)
        if "xx" in sm:
            continue

        if does_string_fit_row(sm, row):
            nums = sm.split("x")
            for num in nums:
                if num == "":
                    continue
                if num[0] == "0" or len(num) == 1:
                    break
                if num != num[::-1]:
                    break
                if int(num) % 23 != 0:
                    break
            else:
                final_strings.append(sm)
                print("Found a good string:", sm)
                with open("row_8.json", "w") as f:
                    json.dump(final_strings, f)


with open("row_8.json", "w") as f:
    json.dump(final_strings, f)


good_strings = []
for s in tqdm.tqdm(final_strings):
    if does_string_fit_row(s, row):
        good_strings.append(s)

print("total number of good strings:", len(good_strings))


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


print(json.dumps(collect_ith_characters(good_strings), indent=1))
