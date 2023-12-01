# quiz1

puzzle_file = open("input.txt", "r")
puzzle_txt = puzzle_file.read()
puzzle_lines = puzzle_txt.split("\n")
num_lines1 = []

for line in puzzle_lines:
    extracted_num = "".join(filter(str.isdigit, line))
    calibration_value = int(f"{extracted_num[:1]}{extracted_num[-1]}")
    num_lines1.append(calibration_value)

result1 = sum(num_lines1)


# quiz2

num_lines2 = []
num_dict = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9
}

for line in puzzle_lines:
    for key in num_dict:
        if key in line:
            print(f"input: {line}, num: {num_dict[key]}")

    extracted_num = "".join(filter(str.isnumeric, line))
    calibration_value = int(f"{extracted_num[:1]}{extracted_num[-1]}")
    # print(f"input: {line}, value: {extracted_num}, output: {calibration_value}")

puzzle_file.close()
