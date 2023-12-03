def check_neighbourhood(lines, row: int, i: int, j: int):
    up = max(0, row - 1)
    down = min(len(lines) - 1, row + 1)
    left = max(0, i - 1)
    right = min(len(lines[row]) - 1, j + 1)
    for r in range(up, down + 1):
        for c in range(left, right):
            char = lines[r][c]
            if not (char.isdigit() or char == "."):
                return True

    return False


def parse_number(line, i):
    while i < len(line) and line[i].isdigit():
        i += 1
    return i


with open(0) as f:
    lines = f.readlines()
result = 0
for row, line in enumerate(lines):
    i = 0
    while i < len(line):
        if line[i].isdigit():
            j = parse_number(line, i)
            if check_neighbourhood(lines, row, i, j):
                number = int(line[i:j])
                result += number
            i = j
        else:
            i += 1

print(result)
