import itertools
import json

ROW = 9

# step 9: find fitting strings for row (product ends in 1)
rows = {
    0: [0, 0, 1, 0, 0, 1, 0, 1, 0, 0],
    8: [0, 1, 1, 1, 1, 0, 1, 0, 1, 1],
    9: [0, 1, 0, 0, 1, 0, 1, 0, 0, 0],  # right
    10: [1, 0, 1, 0, 0, 1, 1, 0, 0, 1],  # right
    11: [0, 0, 0, 0, 1, 0, 0, 1, 0, 1],  # right
}

cols = {
    "8_9": [0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0],
    "9_10": [0, 1, 0, 1, 1, 1, 0, 0, 0, 0, 1],
}

row = rows[ROW]


options = [
    "x1379",
    "1379",
    "x1379",
    "x1379",
    "x1379",
    "x1379",
    "x1379",
    "x1379",
    "x1379",
    "1379",
    "x1379",
]

tot = 1
for option in options:
    tot *= len(option)

# Generate all combinations
all_combinations = itertools.product(*options)


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


# Print each combination as a string
i = 0
WINS = []
for combination in all_combinations:
    s = "".join(combination)
    i += 1
    if i % (int(tot / 100)) == 0:
        print("Percent", int(i * 100 / tot))
        with open(f"row_{ROW}.json", "w") as f:
            json.dump(WINS, f)

    if does_string_fit_row(s, row):
        nums = s.split("x")
        for num in nums:
            if num == "":
                continue
            if len(num) == 1 or num[0] == "0":
                break

            digits = [int(d) for d in num]
            product = 1
            for d in digits:
                product *= d

            if product % 10 != 1:
                break
        else:
            WINS.append(s)


with open(f"row_{ROW}.json", "w") as f:
    json.dump(WINS, f)

print("Done")
