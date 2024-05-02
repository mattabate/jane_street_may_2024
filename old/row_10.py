import itertools
import json

row = [1, 0, 1, 0, 0, 1, 1, 0, 0, 1]


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


# Options for each character position
c1_options = "123456789x"
c2_options = "0123456789"
c3_options = "71x"
c4_options = "0123456789x"
c5_options = "0123456789x"
c6_options = "0123456789x"
c7_options = "37x"
c8_options = "91x"
c9_options = "91x"
c10_options = "91"
c11_options = "02468x"

# Use itertools.product to generate combinations
options = [
    c1_options,
    c2_options,
    c3_options,
    c4_options,
    c5_options,
    c6_options,
    c7_options,
    c8_options,
    c9_options,
    c10_options,
    c11_options,
]

# Generate all combinations
all_combinations = itertools.product(*options)

# Print each combination as a string
i = 0
good_combinations = []
for combination in all_combinations:
    s = "".join(combination)
    i += 1
    if i % 1423105 == 0:
        print("Percent", i / (142310520))
        with open("row_10.json", "w") as f:
            json.dump(good_combinations, f)

    nums = s.split("x")
    for num in nums:
        if num == "":
            continue
        if num[0] == "0" or len(num) == 1:
            break

        if int(num) % 88 != 0:
            break
    else:
        if does_string_fit_row(s, row):
            good_combinations.append(s)
            print("Found a good string:", s)