from collections import defaultdict


def check_neighbourhood(lines, row: int, i: int, j: int):
    up = max(0, row - 1)
    down = min(len(lines) - 1, row + 1)
    left = max(0, i - 1)
    right = min(len(lines[row]) - 1, j + 1)
    result = list()
    for r in range(up, down + 1):
        for c in range(left, right):
            char = lines[r][c]
            if char == "*":
                result.append((r, c))

    return result


def parse_number(line, i):
    while i < len(line) and line[i].isdigit():
        i += 1
    return i


with open(0) as f:
    lines = f.readlines()
result = 0
dct = dict()
for row, line in enumerate(lines):
    i = 0
    while i < len(line):
        if line[i].isdigit():
            j = parse_number(line, i)
            stars = check_neighbourhood(lines, row, i, j)
            number = int(line[i:j])
            for star in stars:
                if star in dct:
                    result += dct[star] * number
                    del dct[star]
                else:
                    dct[star] = number
            i = j
        else:
            i += 1
print(result)
