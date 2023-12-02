import sys


def solution():
    result = 0
    for line in sys.stdin.readlines():
        i = 0
        while not (first := line[i]).isdigit():
            i += 1
        i = len(line) - 1
        while not (second := line[i]).isdigit():
            i -= 1
        result += int(first) * 10 + int(second)
    print(result)


if __name__ == "__main__":
    solution()
