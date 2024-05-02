import itertools
import tqdm
import json
import os
import fire

POS_FILE = "possibilities.json"
VALUES_FILE = "values.json"

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


if not os.path.exists(POS_FILE):
    with open(POS_FILE, "w") as f:
        json.dump({}, f)

if not os.path.exists(VALUES_FILE):
    with open(VALUES_FILE, "w") as f:
        json.dump({}, f)


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


def get_rows(row):
    out = []

    if row == 8:
        with open(VALUES_FILE, "r") as f:
            data = json.load(f)

        options = ["0123456789x" for _ in range(11)]
        options[0] = options[0].replace("0", "")
        options[1] = options[1].replace("x", "")
        options[9] = options[1].replace("x", "")

        if str(row - 1) in data.keys() and f"{row-1}_{row}" in cols.keys():
            # if the row above you has bee characterized
            # if the column openings between the two rows has been characterized
            col_openings = cols[f"{row-1}_{row}"]

            for i, values in enumerate(data[row - 1]):
                # for eventry entry
                "3x179"  # values possible values above you
                "0123456789x"  # current possibilities

                if values == "x":
                    options[i] == options[i].replace("x", "")

                elif len(values) == 1 and col_openings[i] == 1:
                    options[i] = options[i].replace(values, "")

                elif len(values) == 1 and col_openings[i] == 0:
                    # remove every
                    1

                if "x" not in values and col_openings[i] == 0:
                    thing = set()
                    thing.union(set([g for g in values])).union(set("x"))

                    current = set([c for c in options[i]])

                    thing = "".join(list(current.intersection(thing)))
                    options[i] = thing

        if str(row + 1) in data.keys() and f"{row}_{row+1}" in cols.keys():
            # if the row above you has bee characterized
            # if the column openings between the two rows has been characterized
            col_openings = cols[f"{row}_{row+1}"]

            for i in range(11):
                # for eventry entry
                values = data[str(row + 1)][i]
                if "x" not in values and col_openings[i] == 0:
                    thing = options[i]
                    options[i] = "".join([c for c in thing if c in values + "x"])

        # Generate all combinations
        all_combinations = itertools.product(*options)

        tot = 1
        for option in options:
            tot *= len(option)

        print(f"Generating Strings {tot}\n")

        for i, combination in enumerate(all_combinations):
            if i % (int(tot / 100)) == 0:
                # go up one line
                print(f"\033[A{int(i * 100 / tot)}%   ")
            s = "".join(combination)
            out.append(s)

    if row == 9:
        # Define the digits to use
        digits = ["x", "1", "3", "7", "9"]

        # Generate all possible combinations of these digits in strings of length 11
        out = [
            "".join(combination) for combination in itertools.product(digits, repeat=11)
        ]

        # Define the character sets for the different positions
        set1 = "1379x"
        set2 = "0123456789x"  # Characters for positions 0, 2, 5, 7

        # length 5 for "1379x"
        strings_set1 = ["".join(p) for p in itertools.product(set1, repeat=5)]
        # len 6 for set "0123456789x"
        strings_set2 = ["".join(p) for p in itertools.product(set2, repeat=6)]

        new_set1 = []
        for s in strings_set1:
            if s[3] != "x" and s[4] != "x" and s[3] != s[4]:
                continue
            new_set1.append(s)
        strings_set1 = new_set1

        new_set2 = []
        for s in strings_set2:
            if s[1] != "x" and s[2] != "x" and s[1] == s[2]:
                continue
            new_set2.append(s)

    elif row == 10:
        with open(VALUES_FILE, "r") as f:
            data = json.load(f)

        options = ["0123456789x" for _ in range(11)]

        if row - 1 in data.keys() and f"{row-1}_{row}" in cols.keys():
            # if the row above you has bee characterized
            # if the column openings between the two rows has been characterized
            col_openings = cols[f"{row-1}_{row}"]

            for i, values in enumerate(data[row - 1]):
                # for eventry entry
                "3x179"  # values possible values above you
                "0123456789x"  # current possibilities

                if values == "x":
                    options[i] == options[i].replace("x", "")

                elif len(values) == 1 and col_openings[i] == 1:
                    options[i] = options[i].replace(values, "")

                elif len(values) == 1 and col_openings[i] == 0:
                    # remove every
                    1

                if "x" not in values and col_openings[i] == 0:
                    thing = set()
                    thing.union(set([g for g in values])).union(set("x"))

                    current = set([c for c in options[i]])

                    thing = "".join(list(current.intersection(thing)))
                    options[i] = thing

        options = [
            "0123456789x",
            "0123456789",
            "71x",
            "0123456789x",
            "0123456789x",
            "0123456789x",
            "37x",
            "91x",
            "91x",
            "91",
            "02468x",
        ]

        # Generate all combinations
        all_combinations = itertools.product(*options)

        print("Generating Strings\n")
        tot = 1
        for option in options:
            tot *= len(option)

        for i, combination in enumerate(all_combinations):
            if i % (int(tot / 100)) == 0:
                # go up one line
                print(f"\033[A{int(i * 100 / tot)}%   ")
            s = "".join(combination)
            out.append(s)

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


def main(ROW: int):
    all_strings = get_rows(ROW)

    row = rows[ROW]

    good_strings = []
    for string in tqdm.tqdm(all_strings):
        if does_string_fit_row(string, row):
            nums = string.split("x")
            for num in nums:
                if num == "":
                    continue
                if num[0] == "0" or len(num) == 1:
                    break

                if ROW == 8:
                    if num != num[::-1] or int(num) % 23 != 0:
                        break
                elif ROW == 9:
                    # product of digits ends in 1
                    product = 1
                    for char in num:
                        if char.isdigit():
                            product *= int(char)

                    if product % 10 != 1:
                        break
                elif ROW == 10:
                    # must be divisible by 88
                    if int(num) % 88 != 0:
                        break
            else:
                good_strings.append(string)

    print("total number of good strings:", len(good_strings))

    with open(POS_FILE, "r") as f:
        data = json.load(f)

    data[str(ROW)] = good_strings
    with open(POS_FILE, "w") as f:
        json.dump(data, f, indent=2)

    collect = get_options_for_cells(good_strings)
    print(json.dumps(collect, indent=1))

    with open(VALUES_FILE, "r") as f:
        data = json.load(f)

    data[str(ROW)] = collect

    with open(VALUES_FILE, "w") as f:
        json.dump(data, f, indent=2)


if __name__ == "__main__":
    fire.Fire(main)
