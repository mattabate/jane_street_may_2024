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

row = rows[ROW]


options = [
    "x123456789",
    "1379",
    "x0123456789",
    "x0123456789",
    "x0123456789",
    "x0123456789",
    "x0123456789",
    "x0123456789",
    "x0123456789",
    "0123456789",
    "x0123456789",
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
        if "x" != s[j] and "x" != s[j + 1]:
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
            "Time Remaining",
            int((time.time() - t0) / i * (tot - i)),
        )
        with open(f"row_{ROW}.json", "w") as f:
            json.dump(WINS, f, indent=2)

    if does_string_fit_row(s, row):
        nums = s.split("x")
        for num in nums:
            if num == "":
                continue
            if len(num) == 1 or num[0] == "0":
                break

            if num != num[::-1]:
                break
            if int(num) % 23 != 1:
                break
        else:
            WINS.append(s)


with open(f"row_{ROW}.json", "w") as f:
    json.dump(WINS, f, indent=2)

print("Done")
