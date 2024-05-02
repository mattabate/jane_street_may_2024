import itertools
import tqdm
import json


ROW = 9

rows = {9: [0, 1, 0, 0, 1, 0, 1, 0, 0, 0]}


row = rows[ROW]


def check_x_spacing(s):
    # Iterate over the string until the third-last character
    for i in range(len(s) - 2):
        # Check if the current character and the character two positions later are both 'x'
        if s[i] == "x" and s[i + 2] == "x":
            return True
    return False


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
            if check_x_spacing(s):
                return False

    return True


def get_rows(row):
    if row == 9:
        # Define the digits to use
        digits = ["x", "1", "3", "7", "9"]

        # Generate all possible combinations of these digits in strings of length 11
        out = [
            "".join(combination) for combination in itertools.product(digits, repeat=11)
        ]
    return out


def get_options_for_cells(strings):
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


all_strings = get_rows(ROW)

good_strings = []
for string in tqdm.tqdm(all_strings):
    if does_string_fit_row(string, row):
        nums = string.split("x")
        for num in nums:
            if num == "":
                continue
            if num[0] == "0":
                break

            # check criteria
            if ROW == 9:
                # product of digits ends in 1
                product = 1
                for char in num:
                    if char.isdigit():
                        product *= int(char)

                if product % 10 != 1:
                    break
        else:

            good_strings.append(string)


print("total number of good strings:", len(good_strings))
with open(f"row_{ROW}.json", "w") as f:
    json.dump(good_strings, f)

collect = get_options_for_cells(good_strings)
print(json.dumps(collect, indent=1))
