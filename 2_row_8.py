import itertools
import json
import time

ROW = 8

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
    "123456789x",
    "1379",
    "0123456789x",
    "0123456789x",
    "1973x",
    "0123456789x",
    "1973x",
    "0123456789x",
    "1973x",
    "0123456789",
    "1973x",
]

tot = 1
for option in options:
    tot *= len(option)

# Generate all combinations
all_combinations = itertools.product(*options)


def does_string_fit_row(s: str, row: list):
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
t0 = time.time()
for combination in all_combinations:
    s = "".join(combination)
    i += 1
    if i % (int(tot / 100)) == 0:
        print(
            "Percent",
            int(i * 100 / tot),
            "time remaining",
            int((time.time() - t0) / i * (tot - i)),
        )
        with open(f"row_{ROW}.json", "w") as f:
            json.dump(WINS, f)

    if does_string_fit_row(s, row):
        nums = s.split("x")
        for num in nums:
            if num == "":
                continue
            if len(num) == 1 or num[0] == "0":
                break

            if num != num[::-1] or (int(num) % 23 != 0):
                break
        else:
            WINS.append(s)


with open(f"row_{ROW}.json", "w") as f:
    json.dump(WINS, f)

print("Done")
